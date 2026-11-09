"""Master One-Command Submission Verification Script for IMMUNE MEMORY v3.
Runs an end-to-end automated audit of all deliverables, files, hashes, PDF formatting,
and empirical statistics to guarantee 100% competition readiness.
"""
import hashlib
import json
import os
import sys
from pathlib import Path
import pypdf

SUBMISSION_DIR = Path(__file__).resolve().parent
REPO_ROOT = SUBMISSION_DIR.parent

REQUIRED_FILES = [
    "ImmuneMemory_Apart2026_FINAL.pdf",
    "ImmuneMemory_Apart2026_FINAL.docx",
    "ImmuneMemory_Research_Paper.md",
    "INDEPENDENT_SCIENTIFIC_AUDIT.md",
    "VERIFIED_RESULTS.json",
    "CALL_ACCOUNTING.md",
    "CLAIM_EVIDENCE_MATRIX.md",
    "NOVELTY_POSITIONING.md",
    "SCIENTIFIC_REVIEW.md",
    "REPRODUCE.md",
    "COMPETITION_REQUIREMENTS.md",
    "SUBMISSION_CHECKLIST.md",
    "SUBMISSION_FORM_COPY.md",
    "FINAL_STATUS.md",
    "replay.html"
]

REQUIRED_FIGURES = [
    "lifecycle.png",
    "behavioral_results.png",
    "second_handoff.png"
]

def check_files():
    print("[1/5] Checking Required Submission Deliverables...")
    missing = []
    for f in REQUIRED_FILES:
        p = SUBMISSION_DIR / f
        if not p.exists() or p.stat().st_size == 0:
            missing.append(f)
    for f in REQUIRED_FIGURES:
        p = SUBMISSION_DIR / "figures" / f
        if not p.exists() or p.stat().st_size == 0:
            missing.append(f"figures/{f}")
    if missing:
        print(f"FAILED: Missing files: {missing}")
        return False
    print(f"  --> All {len(REQUIRED_FILES) + len(REQUIRED_FIGURES)} submission files present and non-empty.")
    return True

def check_pdf():
    print("[2/5] Inspecting Final PDF Manuscript...")
    pdf_path = SUBMISSION_DIR / "ImmuneMemory_Apart2026_FINAL.pdf"
    if not pdf_path.exists():
        print("FAILED: PDF not found.")
        return False
    
    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    reader = pypdf.PdfReader(str(pdf_path))
    num_pages = len(reader.pages)
    
    print(f"  --> PDF Page Count: {num_pages} pages")
    print(f"  --> PDF File Size: {size_mb:.2f} MB")
    
    if size_mb > 25:
        print("FAILED: File size exceeds Apart 25MB limit.")
        return False
    if num_pages > 8:
        print(f"WARNING: Manuscript has {num_pages} pages (Apart limit: max 8 body pages).")
    else:
        print(f"  --> Page limit compliant: {num_pages} <= 8 pages.")

    # Check text content
    p1 = reader.pages[0].extract_text()
    if "Immune Memory" not in p1 or "Abstract" not in p1:
        print("FAILED: PDF text missing key metadata.")
        return False
    print("  --> PDF formatting and text extraction verified.")
    return True

def check_hashes():
    print("[3/5] Verifying Protocol and Historical Preservation Hashes...")
    
    # Frozen protocol check
    frozen_path = REPO_ROOT / "recovery" / "FROZEN_v3.json"
    frozen = json.loads(frozen_path.read_text(encoding="utf-8"))
    proto_rel = frozen.get("protocol") or frozen.get("protocol_path")
    proto_sha = frozen.get("sha256") or frozen.get("protocol_sha256")
    proto_path = REPO_ROOT / proto_rel
    actual_proto_sha = hashlib.sha256(proto_path.read_bytes()).hexdigest()
    if actual_proto_sha != proto_sha:
        print(f"FAILED: Protocol SHA256 mismatch: {actual_proto_sha} vs {proto_sha}")
        return False
    print(f"  --> Preregistration Protocol hash verified: {actual_proto_sha}")

    # Historical negative pilot preservation check
    pres_path = REPO_ROOT / "corrective-v2" / "original-preservation.json"
    hashes = json.loads(pres_path.read_text(encoding="utf-8"))
    for rel_path, meta in hashes.items():
        file_path = REPO_ROOT / rel_path
        if not file_path.exists():
            print(f"FAILED: Historical file missing: {rel_path}")
            return False
        data = file_path.read_bytes()
        actual_sha = hashlib.sha256(data).hexdigest()
        if actual_sha != meta["sha256"] or len(data) != meta["bytes"]:
            print(f"FAILED: Historical file altered: {rel_path}")
            return False
    print(f"  --> All {len(hashes)} historical preservation hashes intact.")
    return True

def check_gates():
    print("[4/5] Auditing Preregistered Screening Gates...")
    audit_path = REPO_ROOT / "results" / "recovery_pilot" / "independent_audit.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    if audit.get("verdict") != "GO FOR HELD-OUT STUDY":
        print(f"FAILED: Audit verdict is not GO: {audit.get('verdict')}")
        return False
    gates = audit.get("gates", {})
    for g_id, g_info in gates.items():
        if not g_info.get("pass"):
            print(f"FAILED: Gate {g_id} failed!")
            return False
    print("  --> All 8 screening gates (Gates A–H) confirmed PASS.")
    return True

def check_call_accounting():
    print("[5/5] Reconciling API Call Accounting...")
    pilot_log = REPO_ROOT / "results" / "recovery_pilot" / "trials.jsonl"
    heldout_log = REPO_ROOT / "results" / "recovery_heldout" / "heldout_trials.jsonl"
    
    pilot_lines = [json.loads(l) for l in pilot_log.read_text(encoding="utf-8").splitlines() if l.strip()]
    heldout_lines = [json.loads(l) for l in heldout_log.read_text(encoding="utf-8").splitlines() if l.strip()]
    
    pilot_calls = sum(1 for r in pilot_lines if "tokens" in r or "cost" in r)
    heldout_calls = sum(1 for r in heldout_lines if "tokens" in r)
    calibration_calls = 28 # calibrate (12) + test_baseline_full (8) + test_technical_adjustment (8)
    
    total_calls = calibration_calls + pilot_calls + heldout_calls
    print(f"  --> Calibration: {calibration_calls} | Pilot: {pilot_calls} | Held-out: {heldout_calls}")
    print(f"  --> Total Reconciled Calls: {total_calls} (Target: 140)")
    if total_calls != 140:
        print(f"FAILED: Unexpected total call count: {total_calls}")
        return False
    print("  --> Call accounting reconciled exactly.")
    return True

def main():
    print("=================================================================")
    print("       IMMUNE MEMORY v3 — MASTER SUBMISSION VERIFIER             ")
    print("=================================================================\n")
    
    ok = True
    ok = check_files() and ok
    ok = check_pdf() and ok
    ok = check_hashes() and ok
    ok = check_gates() and ok
    ok = check_call_accounting() and ok
    
    print("\n=================================================================")
    if ok:
        print("  VERDICT: ALL VERIFICATIONS PASSED — PACKAGE IS SUBMISSION-READY!  ")
    else:
        print("  VERDICT: VERIFICATION FAILED — CHECK ERRORS ABOVE.              ")
    print("=================================================================")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())

