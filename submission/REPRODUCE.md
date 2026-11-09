# Reproduction & Verification Guide

**Project:** IMMUNE MEMORY v3 (`immune-memory`)  
**Evaluated Foundation Model:** Google Cloud Vertex AI Gemini 2.5 Pro (`gemini-2.5-pro`)  
**Platform:** Windows 10/11 / POSIX compatible (PowerShell / Bash)  
**Python Runtime:** Python 3.11+  

---

## 1. Environment & Prerequisites

Install required dependencies:
```powershell
pip install google-genai matplotlib python-docx reportlab pypdf
```

Set Google Cloud Vertex AI authentication (Application Default Credentials):
```powershell
# Authenticate via Google Cloud SDK
gcloud auth application-default login
# (Optional) Set quota project if required
gcloud auth application-default set-quota-project project-b97ea65d-c159-4b52-98d
```

---

## 2. Zero-Cost Master Verification (One-Command Automated Audit)

Run the comprehensive automated verification suite:
```powershell
cd C:\Users\kudch\Documents\Codex\2026-11-08\files-pasted-by-the-user-autonomous\outputs\immune-memory
python submission/verify_submission.py
```
This single script verifies:
1. All 18 submission deliverables and figures exist.
2. The final PDF is compliant (7 pages <= 8 pages, < 25 MB).
3. The frozen protocol SHA-256 hash matches byte-for-byte.
4. All 8 historical negative pilot files remain untouched and immutable.
5. All 8 screening gates (Gates A–H) pass with `GO FOR HELD-OUT STUDY`.
6. Exact reconciliation of all 140 model calls.

---

## 3. Detailed Zero-Cost Local Verifications (Manual Step-by-Step)

### A. Verify Historical Preservation Hashes
Verifies that all 8 historical pilot files and negative results remain completely immutable and unmodified:
```powershell
cd C:\Users\kudch\Documents\Codex\2026-11-08\files-pasted-by-the-user-autonomous\outputs\immune-memory
python -c "
import json, hashlib
with open('corrective-v2/original-preservation.json', 'r') as f:
    hashes = json.load(f)
for path, expected in hashes.items():
    with open(path, 'rb') as f:
        data = f.read()
        assert hashlib.sha256(data).hexdigest() == expected['sha256'], f'Hash mismatch: {path}'
        assert len(data) == expected['bytes'], f'Byte count mismatch: {path}'
print(f'ALL {len(hashes)} HISTORICAL PRESERVATION HASHES & BYTES MATCH!')
"
```

### B. Verify Frozen Protocol Specification Hash
Verifies that the executed protocol matches the preregistered protocol `docs/preregistered_pilot_v3.md`:
```powershell
python -c "
import json, hashlib
with open('recovery/FROZEN_v3.json', 'r') as f:
    frozen = json.load(f)
proto_file = frozen.get('protocol') or frozen.get('protocol_path')
expected_sha = frozen.get('sha256') or frozen.get('protocol_sha256')
with open(proto_file, 'rb') as f:
    actual_hash = hashlib.sha256(f.read()).hexdigest()
assert actual_hash == expected_sha, 'Protocol hash mismatch!'
print(f'FROZEN PROTOCOL HASH VERIFIED: {actual_hash}')
"
```

### C. Run the Independent Scientific Audit on Raw Pilot Logs
Parses `results/recovery_pilot/trials.jsonl` and evaluates all 8 screening gates (Gates A–H):
```powershell
python recovery/audit.py
```
*Expected Output:* `FINAL AUDIT VERDICT: GO FOR HELD-OUT STUDY` (8/8 Gates Passed).

### D. Re-generate High-Resolution Figures
Generates the publication figures into `submission/figures/`:
```powershell
python submission/make_figures.py
```

### E. Compile the Final Apart PDF
Compiles the formatted academic PDF `submission/ImmuneMemory_Apart2026_FINAL.pdf`:
```powershell
python submission/build_pdf.py
```

---

## 4. Live API Reruns (Billable Cloud Inference)

*Warning: Executing these scripts initiates live API calls to Google Cloud Vertex AI.*

### A. Run Calibration Screen (28 calls, ~$0.012 USD)
```powershell
python recovery/calibrate.py
python recovery/test_technical_adjustment.py
```

### B. Run Preregistered Pilot Evaluation (72 calls, ~$0.070 USD)
```powershell
python recovery/run_pilot.py
```

### C. Run Held-Out Secondary Swarm Propagation (40 calls, ~$0.019 USD)
```powershell
python recovery/run_heldout.py
```

