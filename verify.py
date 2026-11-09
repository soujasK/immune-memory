"""Validate a completed batch against the frozen schedule and independently rescore each decision."""
import argparse
import hashlib
import json
from pathlib import Path

from policy_oracle import score
from scenarios import CASES

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("input", type=Path)
args = parser.parse_args()
rows = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines()]
cases = {case["id"]: case for case in CASES}
expected = {(case, seed, warning, removed) for case in cases for seed in (271, 811)
            for warning in (False, True) for removed in (False, True)}
actual = {(r["case"], r["seed"], r["warning"], r["removed"]) for r in rows}
assert len(rows) == len(expected) and expected == actual
assert [r["index"] for r in rows] == list(range(1, 65))
assert len({r["run_id"] for r in rows}) == 1
hashes = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
          for name in ("pilot.py", "scenarios.py", "policy_oracle.py")}
calls = 0
for row in rows:
    assert row["source_hashes"] == hashes
    case = cases[row["case"]]
    assert case["adversarial"] == row["adversarial"]
    events = row["events"]
    assert [e["agent"] for e in events if e["kind"] == "call"] == list("ABCD" if row["removed"] else "AABCD")
    if row["removed"]:
        assert events[1] == {"kind": "removal", "agent": "A"}
    for event in events:
        if event["kind"] == "call":
            assert "raw" in event
            calls += 1
    raw = json.loads(events[-1]["raw"])["choices"][0]["message"]["content"] or ""
    assert json.loads(json.dumps(score(case, raw))) == row["score"]
print(f"Verified {len(rows)} unique episodes, {calls} provider responses and independent oracle agreement.")

