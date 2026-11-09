"""Verify real trajectories and report paired counts with family-cluster intervals."""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path

from oracle_v2 import score, validate
from scenarios_v2 import task


def percentile(values, p):
    values = sorted(values)
    position = (len(values)-1)*p
    lower = int(position)
    return values[lower] + (position-lower)*(values[min(lower+1,len(values)-1)]-values[lower])


def cluster_interval(family_differences):
    samples = [sum(draw)/4 for draw in itertools.product(family_differences, repeat=4)]
    return [percentile(samples,.025), percentile(samples,.975)]


def analyze(path):
    events = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
    assert events[0]['kind']=='run_start' and not events[0]['preflight']
    assert events[-1]['kind']=='run_complete', 'Incomplete batch'
    for name,digest in events[0]['hashes'].items():
        assert hashlib.sha256(path.parent.parent.joinpath(name).read_bytes()).hexdigest()==digest, name
    outcomes=[e for e in events if e['kind']=='outcome']
    responses=[e for e in events if e['kind']=='response']
    requests=[e for e in events if e['kind']=='request']
    failures=[e for e in events if e['kind']=='failure']
    expected={(f,s,w,a,p,t) for f in range(4) for s in (271,811) for w in (False,True)
              for a in 'BCD' for p in ('pre','post') for t in (False,True)}
    indexed={(e['family'],e['seed'],e['warning'],e['agent'],e['phase'],e['adversarial']):e for e in outcomes}
    assert len(indexed)==len(outcomes), 'Duplicate outcome'
    technical_complete=set(indexed)==expected and not any(e['kind']=='network_invalid' for e in events)
    for event in outcomes:
        matching=[r for r in responses if r['network']==event['network'] and r['agent']==event['agent']
                  and r['stage']==event['phase']+('-attack' if event['adversarial'] else '-legitimate')]
        raw=json.loads(matching[-1]['raw'])['choices'][0]['message']['content']
        assert json.loads(json.dumps(score(event['family'],event['phase'],validate(raw))))==event['score']
    for network in {e['network'] for e in outcomes}:
        trace=[e for e in events if e.get('network')==network]
        removals=[i for i,e in enumerate(trace) if e['kind']=='removal']
        if len(removals)!=1:
            technical_complete=False
            continue
        cut=removals[0]
        pre=[e for e in trace[:cut] if e['kind']=='outcome']
        post=[e for e in trace[cut:] if e['kind']=='outcome']
        assert len(pre)==6 and all(e['phase']=='pre' for e in pre)
        assert all(e['phase']=='post' for e in post)
        assert not any(e.get('agent')=='A' and e['kind'] in ('request','delivery') for e in trace[cut+1:])
        for req in [e for e in trace if e['kind']=='request']:
            if req['stage'].startswith('pre-'):
                assert 'Juniper-' not in json.dumps(req['payload']['messages'])
            if req['stage'].startswith('post-'):
                assert 'Cedar-' in json.dumps(req['payload']['messages'])
            assert 'Gate ' not in json.dumps(req['payload']['messages'])
    cells={}
    for agent,phase,warning,adversarial in itertools.product('BCD',('pre','post'),(False,True),(False,True)):
        group=[e['score'] for e in outcomes if (e['agent'],e['phase'],e['warning'],e['adversarial'])==(agent,phase,warning,adversarial)]
        key=f"{agent}/{phase}/{'warning' if warning else 'neutral'}/{'attack' if adversarial else 'legitimate'}"
        cells[key]=dict(n=len(group),**{metric:sum(g[metric] for g in group) for metric in ('violation','incorrect','complete','success','refusal')})
    comparisons={}
    if technical_complete:
        for phase,adversarial in itertools.product(('pre','post'),(False,True)):
            metric='violation' if adversarial else 'success'
            family_diffs=[]
            transitions=Counter()
            pair_records=[]
            for family in range(4):
                diffs=[]
                for seed in (271,811):
                    neutral=indexed[(family,seed,False,'D',phase,adversarial)]['score']
                    warning=indexed[(family,seed,True,'D',phase,adversarial)]['score']
                    diff=int(neutral[metric])-int(warning[metric])
                    diffs.append(diff)
                    transitions[f'{int(neutral[metric])}->{int(warning[metric])}']+=1
                    pair_records.append(dict(family=family,seed=seed,neutral=neutral,warning=warning))
                family_diffs.append(sum(diffs)/2)
            key=phase+'/'+('attack' if adversarial else 'legitimate')
            comparisons[key]=dict(metric=metric,direction='neutral minus warning',
                difference_count=sum(family_diffs)*2,risk_difference=sum(family_diffs)/4,
                exploratory_95_cluster_bootstrap=cluster_interval(family_diffs),
                leave_one_family_out=[sum(family_diffs[:i]+family_diffs[i+1:])/3 for i in range(4)],
                family_risk_differences=family_diffs,transitions=transitions,pairs=pair_records)
    usage=[json.loads(e['raw']).get('usage',{}) for e in responses]
    totals={k:sum((u.get(k) or 0) for u in usage) for k in ('prompt_tokens','completion_tokens','total_tokens')}
    return dict(technical_complete=technical_complete,outcomes=len(outcomes),cells=cells,comparisons=comparisons,
                requests=len(requests),responses=len(responses),failures=failures,
                retries=sum(e['attempt']>0 for e in requests),tokens=totals,
                response_seconds=sum(e['seconds'] for e in responses)),events


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('output',type=Path)
    args=parser.parse_args()
    summary,events=analyze(args.input)
    args.output.mkdir(parents=True,exist_ok=True)
    (args.output/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    lines=[]
    for e in events:
        if e['kind']=='response' and e['stage'] in ('source','relay'):
            content=json.loads(e['raw'])['choices'][0]['message']['content']
            lines.append(f"{e['network']} | {e['agent']} | attempt {e['attempt']}\n{content}\n")
    (args.output/'relay-review.txt').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('cells','comparisons','failures')},indent=2))
    print(json.dumps({k:v for k,v in summary['cells'].items() if k.startswith('D/')},indent=2))


if __name__=='__main__':
    main()
