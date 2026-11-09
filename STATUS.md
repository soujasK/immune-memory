# IMMUNE MEMORY Research Checkpoint & Status

**Document Date:** November 8, 2026  
**Active Phase:** Recovery Evaluation Complete (Protocol v3.0)  
**Evaluated Model:** Google Cloud Vertex AI Gemini 2.5 Pro (`gemini-2.5-pro`, `us-central1`)  
**Audit Verdict:** **GO FOR HELD-OUT STUDY — 8/8 GATES PASSED**  
**Cumulative Spend:** **$0.0812 USD** (Total Budget Cap: $5.00 USD)  
**Historical Integrity:** All original pilot files and hashes remain 100% verified and immutable.

---

## 1. Historical Pilot Status & Forensic Preservation
- The original pilot (Dolphin Llama 3 8B, 42 evaluated episodes) remains preserved and fingerprinted in `corrective-v2/original-preservation.json`.
- A comprehensive forensic postmortem is recorded in [`docs/original_pilot_postmortem.md`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/docs/original_pilot_postmortem.md), documenting:
  - Technical defects: token truncation at `max_tokens: 100`, unhandled formatting fences.
  - Protocol defects: inverted temporal sequencing where Agent A was removed before message delivery to Agent B, leaving zero pre-removal uptake.
  - Historical verdict: **NO-GO** preserved.

---

## 2. Recovery Evaluation Architecture (Protocol v3.0)
- **Operational Memory Definition:** Physically grounded in Conversational-History Retention. Evaluated against the 6-level behavioral ladder (Level A to F), rejecting sentiment-based scoring. Documented in [`docs/novelty_reassessment.md`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/docs/novelty_reassessment.md).
- **Preregistered Protocol:** Frozen in [`docs/preregistered_pilot_v3.md`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/docs/preregistered_pilot_v3.md) and fingerprinted in [`recovery/FROZEN_v3.json`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/recovery/FROZEN_v3.json) (SHA-256: `fccae917ed4205e5d9bea245a207d9d02d3a2b57589e5bd0b5999539a46bf3c4`).
- **4-Arm Matched Design:**
  - **Treatment W:** Peer Warning Memo $\to$ Uptake on $t_1$ $\to$ Source $A$ Severed $\to$ Persistence on $t_2$.
  - **Control N:** Peer Neutral Memo $\to$ Uptake on $t_1$ $\to$ Source $A$ Severed $\to$ Persistence on $t_2$.
  - **Control F:** Fresh Agent $B$ on $t_2$.
  - **Control D:** Direct System Warning Directive on $t_1 \to t_2$.

---

## 3. Empirical Results Summary

### A. Pilot Phase ($N=4$ Scenario Pairs, 56 Decisions)
| Experimental Arm | Immediate Uptake ($t_1$) | Post-Removal Test ($t_2$) | Legitimate Success | False Refusals |
| :--- | :---: | :---: | :---: | :---: |
| **Treatment W (Peer Warning)** | **0/4 (0.0% violations)** | **0/4 (0.0% violations)** | **8/8 (100.0%)** | 0/8 (0.0%) |
| **Control N (Peer Neutral)** | 3/4 (75.0% violations) | 3/4 (75.0% violations) | 8/8 (100.0%) | 0/8 (0.0%) |
| **Control F (Fresh Baseline)** | N/A | 4/4 (100.0% violations) | 4/4 (100.0%) | 0/4 (0.0%) |
| **Control D (Direct Directive)** | 0/4 (0.0% violations) | 0/4 (0.0% violations) | 8/8 (100.0%) | 0/8 (0.0%) |

### B. Held-Out Confirmation Phase ($N=4$ Scenarios, 24 Decisions)
| Condition | Secondary Propagation ($t_3$) | Legitimate Success | False Refusals |
| :--- | :---: | :---: | :---: |
| **Protective Handoff ($A \to B \to C$)** | **0/4 (0.0% violations)** | **4/4 (100.0%)** | 0/4 (0.0%) |
| **Neutral Handoff ($A_{\text{neut}} \to B \to C$)** | 2/4 (50.0% violations) | 4/4 (100.0%) | 0/4 (0.0%) |
| **Fresh Agent $C$ Baseline** | 2/4 (50.0% violations) | 4/4 (100.0%) | 0/4 (0.0%) |

---

## 4. Screening Gate Audit Verdict
All 8 preregistered screening gates passed objectively in [`results/recovery_pilot/independent_audit.json`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/results/recovery_pilot/independent_audit.json):
- **Gate A (Technical Validity):** PASS (56/56 valid schemas, 0 parse errors)
- **Gate B (Model Competence):** PASS (100% legitimate task completion, 0 false refusals)
- **Gate C (Informative Baseline):** PASS (Control F: 100% violations, Control N: 75% violations)
- **Gate D (Genuine Uptake):** PASS (8/8 sequences completed before source removal)
- **Gate E (Behavioral Signal $t_1$):** PASS (0% Arm W vs. 75% Arm N)
- **Gate F (Persistence $t_2$):** PASS (0% Arm W vs. 75% Arm N)
- **Gate G (Novelty & Mechanism):** PASS (Conversational-history retention isolated)
- **Gate H (Replication Feasibility):** PASS (Total spend ~$0.08 vs. $5.00 limit)

---

## 5. Artifacts and Deliverables
- **Scientific Research Paper:** [`report/paper.md`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/report/paper.md) (16 sections, Apart formatting compliant)
- **Figure 1:** [`report/figure1_persistence_matrix.png`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/report/figure1_persistence_matrix.png)
- **Figure 2:** [`report/figure2_utility_and_lifecycle.png`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/report/figure2_utility_and_lifecycle.png)
- **Audit Reports:** [`docs/original_pilot_postmortem.md`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/docs/original_pilot_postmortem.md), [`docs/novelty_reassessment.md`](file:///c:/Users/kudch/Documents/Codex/2026-11-08/files-pasted-by-the-user-autonomous/outputs/immune-memory/docs/novelty_reassessment.md)
- **Execution Code:** `recovery/gemini_client.py`, `recovery/oracle.py`, `recovery/scenarios.py`, `recovery/calibrate.py`, `recovery/run_pilot.py`, `recovery/run_heldout.py`, `recovery/audit.py`, `recovery/generate_figures.py`.
