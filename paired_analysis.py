"""Report paired outcomes and missing-outcome bounds without treating seeds as independent cases."""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("summary", type=Path)
args = parser.parse_args()
summary = json.loads(args.summary.read_text(encoding="utf-8"))
output = {}
for state in ("retained", "removed"):
    control = summary["cells"]["Neutral / " + state]
    warning = summary["cells"]["Warning / " + state]
    difference = control["unauthorized_adversarial"] - warning["unauthorized_adversarial"]
    transitions = Counter()
    by_family = defaultdict(Counter)
    for key, pair in summary["pairs"].items():
        case, _, source_state = key.split(" / ")
        if source_state != state or not case.endswith("-X"):
            continue
        statuses = []
        for arm in ("neutral", "warning"):
            score = (pair.get(arm) or {}).get("score") or {}
            statuses.append(str(score["violation"]) if score.get("valid") else "unknown")
        transition = " → ".join(statuses)
        transitions[transition] += 1
        by_family[case[:-2]][transition] += 1
    missing_control = 8 - control["adversarial_observed"] + control["invalid_adversarial"]
    missing_warning = 8 - warning["adversarial_observed"] + warning["invalid_adversarial"]
    output[state] = {
        "control_minus_warning_recorded_violations": difference,
        "control_minus_warning_missing_outcome_bounds": [difference - missing_warning,
                                                         difference + missing_control],
        "legitimate_success_warning_minus_control": warning["legitimate_success"] - control["legitimate_success"],
        "paired_adversarial_transitions_neutral_to_warning": transitions,
        "paired_adversarial_transitions_by_family": by_family,
    }
print(json.dumps(output, indent=2, ensure_ascii=True))

