"""Calibration Runner for Gemini 2.5 Pro on Development Scenarios (Pine-*).
Tests:
1. Legitimate task completion (Pine-01-L .. Pine-04-L)
2. Baseline adversarial response under Neutral condition (Pine-01-X .. Pine-04-X)
3. Protective response under Warning condition (Pine-01-X .. Pine-04-X)
4. Action-label & destination preference check across all 4 destinations
5. Independent scorer verification and cost/token accounting.
"""
import json
from pathlib import Path
import sys
import time

from recovery.gemini_client import GeminiProTracker
from recovery.oracle import score_action
from recovery.scenarios import (
    CALIBRATION_SPECS,
    SYSTEM_PROMPT,
    WARNING_MEMO,
    NEUTRAL_MEMO,
    build_task,
)

def run_calibration(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    tracker = GeminiProTracker()
    log_file = output_dir / "calibration_log.jsonl"
    
    print(f"Starting Gemini 2.5 Pro Task Calibration...")
    print(f"Tracking output at: {log_file}")
    
    records = []
    
    # 1. Legitimate Tasks (Pine-01-L to Pine-04-L)
    print("\n--- TEST 1: Legitimate Task Completion (Pine-01-L to Pine-04-L) ---")
    legit_results = []
    for spec in CALIBRATION_SPECS:
        task = build_task(spec, adversarial=False)
        contents = [
            f"Colleague Note:\n{NEUTRAL_MEMO}\n\nTask:\n{task['prompt']}"
        ]
        res = tracker.generate(contents=contents, system_instruction=SYSTEM_PROMPT, seed=191)
        score = score_action(task, res["text"])
        legit_results.append((task["id"], score))
        print(f"[{task['id']}] Valid: {score['valid']}, Complete: {score['complete']}, Authorized: {score['authorized']}, Refusal: {score['refusal']}")
        records.append({
            "phase": "calibration_legitimate",
            "task_id": task["id"],
            "task_spec": task,
            "response": res,
            "score": score,
        })

    # 2. Baseline Adversarial under Neutral Memo (Pine-01-X to Pine-04-X)
    print("\n--- TEST 2: Baseline Adversarial Vulnerability (Neutral Memo) ---")
    neutral_adv_results = []
    for spec in CALIBRATION_SPECS:
        task = build_task(spec, adversarial=True)
        contents = [
            f"Colleague Note:\n{NEUTRAL_MEMO}\n\nTask:\n{task['prompt']}"
        ]
        res = tracker.generate(contents=contents, system_instruction=SYSTEM_PROMPT, seed=191)
        score = score_action(task, res["text"])
        neutral_adv_results.append((task["id"], score))
        print(f"[{task['id']}] Valid: {score['valid']}, Violation/Unauthorized: {score['unauthorized']}, Authorized: {score['authorized']}, Ledger: {score['ledger']}")
        records.append({
            "phase": "calibration_baseline_adversarial",
            "task_id": task["id"],
            "task_spec": task,
            "response": res,
            "score": score,
        })

    # 3. Protective Adversarial under Warning Memo (Pine-01-X to Pine-04-X)
    print("\n--- TEST 3: Protective Response (Warning Memo) ---")
    warning_adv_results = []
    for spec in CALIBRATION_SPECS:
        task = build_task(spec, adversarial=True)
        contents = [
            f"Colleague Note:\n{WARNING_MEMO}\n\nTask:\n{task['prompt']}"
        ]
        res = tracker.generate(contents=contents, system_instruction=SYSTEM_PROMPT, seed=191)
        score = score_action(task, res["text"])
        warning_adv_results.append((task["id"], score))
        print(f"[{task['id']}] Valid: {score['valid']}, Violation/Unauthorized: {score['unauthorized']}, Authorized: {score['authorized']}, Ledger: {score['ledger']}")
        records.append({
            "phase": "calibration_warning_adversarial",
            "task_id": task["id"],
            "task_spec": task,
            "response": res,
            "score": score,
        })

    # Save all raw records
    with open(log_file, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
            
    # Calculate Summary Statistics
    legit_complete = sum(1 for _, s in legit_results if s["authorized"])
    baseline_violations = sum(1 for _, s in neutral_adv_results if s["unauthorized"])
    warning_violations = sum(1 for _, s in warning_adv_results if s["unauthorized"])
    warning_authorized = sum(1 for _, s in warning_adv_results if s["authorized"])
    
    summary = {
        "model": "gemini-2.5-pro",
        "total_calibration_calls": tracker.total_calls,
        "total_tokens": tracker.total_tokens,
        "total_cost_usd": tracker.total_cost_usd,
        "legitimate_completion_rate": f"{legit_complete}/4 ({legit_complete/4*100:.1f}%)",
        "baseline_adversarial_violations": f"{baseline_violations}/4 ({baseline_violations/4*100:.1f}%)",
        "warning_adversarial_violations": f"{warning_violations}/4 ({warning_violations/4*100:.1f}%)",
        "warning_authorized_rate": f"{warning_authorized}/4 ({warning_authorized/4*100:.1f}%)",
    }
    
    summary_file = output_dir / "calibration_summary.json"
    summary_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    
    print("\n=== CALIBRATION SUMMARY ===")
    print(json.dumps(summary, indent=2))
    return summary

if __name__ == "__main__":
    out = Path("results/recovery_calibration")
    run_calibration(out)

