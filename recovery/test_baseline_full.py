"""Empirical Baseline Vulnerability Test across all Pilot Scenarios (Cedar-* and Juniper-*).
Tests whether Gemini 2.5 Pro exhibits any baseline vulnerability under Neutral condition.
"""
import json
from pathlib import Path
from recovery.gemini_client import GeminiProTracker
from recovery.oracle import score_action
from recovery.scenarios import (
    PILOT_PRE_SPECS,
    PILOT_POST_SPECS,
    SYSTEM_PROMPT,
    NEUTRAL_MEMO,
    build_task,
)

def test_full_baseline():
    tracker = GeminiProTracker()
    all_specs = [("PRE", s) for s in PILOT_PRE_SPECS] + [("POST", s) for s in PILOT_POST_SPECS]
    
    print(f"Testing baseline vulnerability across all {len(all_specs)} pilot adversarial scenarios...")
    results = []
    
    for phase, spec in all_specs:
        task = build_task(spec, adversarial=True)
        contents = [f"Colleague Note:\n{NEUTRAL_MEMO}\n\nTask:\n{task['prompt']}"]
        res = tracker.generate(contents=contents, system_instruction=SYSTEM_PROMPT, seed=191)
        score = score_action(task, res["text"])
        results.append({
            "phase": phase,
            "id": task["id"],
            "score": score,
            "text": res["text"],
            "tokens": res["total_tokens"],
            "cost": res["cost_usd"]
        })
        print(f"[{phase}][{task['id']}] Violation: {score['unauthorized']}, Authorized: {score['authorized']}, Ledger: {score['ledger']}")

    total_violations = sum(1 for r in results if r["score"]["unauthorized"])
    total_authorized = sum(1 for r in results if r["score"]["authorized"])
    
    summary = {
        "model": "gemini-2.5-pro",
        "total_cases": len(results),
        "total_violations": total_violations,
        "total_authorized": total_authorized,
        "violation_rate": f"{total_violations}/{len(results)} ({total_violations/len(results)*100:.1f}%)",
        "total_tokens": tracker.total_tokens,
        "total_cost_usd": tracker.total_cost_usd
    }
    
    out_path = Path("results/recovery_calibration/baseline_pilot_screen.json")
    out_path.write_text(json.dumps({"summary": summary, "results": results}, indent=2), encoding="utf-8")
    print("\n=== PILOT BASELINE SCREEN RESULT ===")
    print(json.dumps(summary, indent=2))
    return summary

if __name__ == "__main__":
    test_full_baseline()

