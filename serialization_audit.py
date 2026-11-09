"""Post-hoc serialization audit. This never changes the frozen primary score."""
import argparse
import json
from collections import Counter
from pathlib import Path
from policy_oracle import score
from scenarios import CASES
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("input",type=Path)
args=parser.parse_args()
cases={c["id"]:c for c in CASES}
records=[]
for line in args.input.read_text(encoding="utf-8").splitlines():
    row=json.loads(line)
    if row.get("score",{}).get("valid"):
        continue
    final=row["events"][-1]
    body=json.loads(final["raw"])
    text=body["choices"][0]["message"]["content"] or ""
    candidates=[]
    for offset,char in enumerate(text):
        if char!="{":
            continue
        try:
            obj,end=json.JSONDecoder().raw_decode(text[offset:])
        except ValueError:
            continue
        candidate=score(cases[row["case"]],json.dumps(obj))
        if candidate["valid"]:
            candidates.append(dict(offset=offset,end=offset+end,object=obj,hypothetical_score=candidate))
    records.append(dict(index=row["index"],case=row["case"],seed=row["seed"],
                        warning=row["warning"],removed=row["removed"],
                        finish_reason=body["choices"][0].get("finish_reason"),
                        candidates=candidates))
print(json.dumps({"status":"Exploratory post-hoc audit of text, not executed actions",
                  "invalid_count":len(records),
                  "single_recoverable_object":sum(len(r["candidates"])==1 for r in records),
                  "records":records},indent=2))
