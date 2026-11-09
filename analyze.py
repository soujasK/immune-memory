"""Summarize recorded outcomes and generate a local trajectory replay."""
import argparse
import html
import json
from pathlib import Path

CELLS = [(False, False), (True, False), (False, True), (True, True)]

def label(warning, removed):
    return ("Warning" if warning else "Neutral") + " / " + ("removed" if removed else "retained")

def summarize(rows):
    cells, pairs = {}, {}
    for warning, removed in CELLS:
        group = [r for r in rows if (r["warning"], r["removed"]) == (warning, removed)]
        attack = [r.get("score", {}) for r in group if r["adversarial"]]
        benign = [r.get("score", {}) for r in group if not r["adversarial"]]
        cells[label(warning, removed)] = {
            "adversarial_observed": len(attack),
            "legitimate_observed": len(benign),
            "invalid_adversarial": sum(not s.get("valid") for s in attack),
            "invalid_legitimate": sum(not s.get("valid") for s in benign),
            "unauthorized_adversarial": sum(s.get("violation") is True for s in attack),
            "legitimate_success": sum(bool(s.get("complete") and s.get("violation") is False) for s in benign),
            "legitimate_false_refusal": sum(s.get("refusal") is True for s in benign),
        }
    for row in rows:
        key = f"{row['case']} / {row['seed']} / {'removed' if row['removed'] else 'retained'}"
        pairs.setdefault(key, {})["warning" if row["warning"] else "neutral"] = {
            "index": row["index"], "score": row.get("score"), "error": row.get("error")}
    calls = [e for r in rows for e in r["events"] if e["kind"] == "call"]
    usage = [json.loads(e["raw"]).get("usage") or {} for e in calls if "raw" in e]
    return {"cells": cells, "pairs": pairs, "call_attempts": len(calls), "responses": len(usage),
            "call_seconds": sum(e["seconds"] for e in calls),
            "tokens": {key: sum(u.get(key, 0) or 0 for u in usage)
                       for key in ("prompt_tokens", "completion_tokens", "total_tokens")}}

def replay(rows, output):
    sections = []
    for r in rows:
        title = f"Trial {r['index']} | {r['case']} | seed {r['seed']} | {label(r['warning'], r['removed'])}"
        body = []
        for e in r["events"]:
            if e["kind"] == "removal":
                body.append("<p><strong>A removed. B retains its earlier note.</strong></p>")
                continue
            request = e["request"]
            response = json.loads(e["raw"])["choices"][0]["message"]["content"] if "raw" in e else "(no response)"
            prompt = "\n\n".join(m["role"] + ": " + m["content"] for m in request["messages"])
            body.append(f"<h3>Agent {e['agent']}</h3><pre>{html.escape(prompt)}</pre>"
                        f"<p>Generated response</p><pre>{html.escape(str(response))}</pre>")
        result = html.escape(json.dumps(r.get("score", {"error": r.get("error")}), indent=2))
        sections.append(f"<details><summary>{html.escape(title)}</summary>{''.join(body)}"
                        f"<h3>Oracle result</h3><pre>{result}</pre></details>")
    output.write_text('<!doctype html><meta charset="utf-8"><title>Immune Memory replay</title>'
                      '<style>body{font:16px system-ui;max-width:900px;margin:3rem auto;padding:0 1rem}'
                      'details,pre{padding:.75rem;background:#eef4f6;margin:.6rem 0}pre{white-space:pre-wrap}'
                      'summary{cursor:pointer}h3{color:#204351}</style><h1>Immune Memory pilot replay</h1>'
                      '<p>Expand a trial to see the actual prompt, generated reply, removal event, and oracle score. '
                      'Compare matching case and seed across warning and neutral conditions.</p>' + ''.join(sections),
                      encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    rows = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines()]
    args.output.mkdir(parents=True, exist_ok=True)
    summary = summarize(rows)
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    replay(rows, args.output / "replay.html")
    print(json.dumps({k: v for k, v in summary.items() if k != "pairs"}, indent=2))

if __name__ == "__main__":
    main()

