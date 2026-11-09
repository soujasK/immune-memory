# Apart Research Swarm Alignment Hackathon 2026 — Submission Readiness Checklist

**Project:** IMMUNE MEMORY v3 (`immune-memory`)  
**Auditor:** Independent Scientific Audit Lead  
**Audit Date:** November 9, 2026 (00:20 IST)  
**Submission Deadline:** Monday, November 9, 2026, at 17:29 IST (23:59 AoE)  

---

## Master Checklist

- [x] **Correct project identified:** Located at `C:\Users\kudch\Documents\Codex\2026-11-08\files-pasted-by-the-user-autonomous\outputs\immune-memory`.
- [x] **Original historical pilot preserved:** `corrective-v2/original-preservation.json` verified with all 8 file hashes and byte counts matching byte-for-byte.
- [x] **All v3 raw evidence located:** `results/recovery_pilot/trials.jsonl` (72 model calls) and `results/recovery_heldout/heldout_trials.jsonl` (40 model calls) intact.
- [x] **Every primary statistic independently verified:** 
  - Arm W: 0/4 violations ($0.0\%$) on $t_1$, 0/4 violations ($0.0\%$) on $t_2$.
  - Control N: 3/4 violations ($75.0\%$) on $t_1$, 3/4 violations ($75.0\%$) on $t_2$.
  - Control F: 4/4 violations ($100.0\%$) on $t_2$.
  - Control D: 0/4 violations ($0.0\%$) on $t_1$, 0/4 violations ($0.0\%$) on $t_2$.
  - Held-out Protective Handoff: 0/4 violations ($0.0\%$) on $t_3$.
  - Held-out Neutral Handoff: 2/4 violations ($50.0\%$) on $t_3$.
  - Held-out Fresh Baseline: 2/4 violations ($50.0\%$) on $t_3$.
- [x] **Total model calls reconciled:** 140 total calls verified (28 calibration + 72 pilot + 40 held-out); transient network error and process resumption on call 34 fully documented.
- [x] **Pilot and held-out datasets correctly distinguished:** Pilot evaluated `Cedar-*` ($t_1$) and `Juniper-*` ($t_2$); Held-Out evaluated `Linden-*` ($t_3$).
- [x] **All four conditions described accurately:** Treatment W (Peer Warning), Control N (Peer Neutral), Control F (Fresh), Control D (Direct Directive).
- [x] **Source-removal timing verified:** Chronological sequence strictly enforced: Stage 2 (Exposure) $\to$ Stage 3 (Uptake $t_1$) $\to$ Stage 4 (Sever Source $A$) $\to$ Stage 5 (Persistence $t_2$).
- [x] **Retained-history mechanism described accurately:** Explicitly framed as Conversational-History Retention; zero claims of parametric weight updates or biological emergence.
- [x] **Direct-warning limitation disclosed:** Control D achieves identical 0/4 violations ($0.0\%$), establishing that peer delivery is sufficient, but not uniquely superior, to direct instruction.
- [x] **Second handoff independently verified:** Stage 7 ($B \to C$) achieves 0/4 violations ($0.0\%$) on held-out tasks.
- [x] **Legitimate-task denominator confirmed:** 40 / 40 legitimate tasks completed successfully ($100.0\%$; 28 pilot + 12 held-out) with 0 / 40 false refusals ($0.0\%$).
- [x] **Closest prior work cited accurately:** Bansal et al. (MSR, 2026), Lee & Tiwari (2024), Cemri et al. (2025, MAST), Peigné et al. (2025).
- [x] **Abstract 150–250 words:** Exactly 211 words in final manuscript (strictly verified in 190–220 and 150–250 ranges).
- [x] **Author information correct:** Soujas Kudchadkar confirmed and embedded into manuscript and submission portal copy.
- [x] **Affiliation correct:** SVKM's NMIMS, Mumbai, India confirmed and embedded into manuscript and submission portal copy.
- [x] **Main paper eight pages or fewer:** Exactly 6 pages total, with pure monochrome styling, booktabs tables, and pure black headings.
- [x] **Required ethical appendix included:** Mandatory Section 'Limitations and Dual-Use / Ethical Considerations' fully detailed.
- [x] **Figures match raw data:** `lifecycle_monochrome.png` and `combined_results_monochrome.png` reflect verified numbers with clean N = 4 labels.
- [x] **PDF visually inspected:** Page count (6 pages), typography (Times New Roman), zero colored pixels, zero blue pixels verified via PyMuPDF at 200 DPI.
- [x] **Official template compliance verified:** Built upon official Apart template v0.9.0 (`report/official-template-v0.9.0.docx`) and compiled to PDF (`submission/ImmuneMemory_Apart2026_FINAL.pdf` and `C:\Users\kudch\Downloads\ImmuneMemory_Apart2026_FINAL.pdf`).
- [x] **No fabricated results:** All data points backed by raw JSONL lines.
- [x] **No fake references:** Real, verified literature citations.
- [x] **Preexisting work disclosed:** Failed historical pilot thoroughly audited in `docs/original_pilot_postmortem.md`.
- [x] **Source code/reproduction instructions available:** Fully documented in `submission/REPRODUCE.md`.
- [x] **Final file path verified:** `submission/ImmuneMemory_Apart2026_FINAL.pdf`.
- [x] **Submission form contents ready:** Prepared in `submission/SUBMISSION_FORM_COPY.md`.
- [ ] **Actual submission completed by user:** Pending final human submission via the Apart portal by the user (scheduled before Monday, Nov 9, 2026, 17:29 IST).

