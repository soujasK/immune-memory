# Call Accounting, Scored Decisions, and Telemetry Reconciliation

**Project:** IMMUNE MEMORY v3 (`immune-memory`)  
**Evaluated Model:** Google Cloud Vertex AI Gemini 2.5 Pro (`gemini-2.5-pro`)  
**Author:** Soujas Kudchadkar (SVKM's NMIMS, Mumbai, India)  
**API Auth & Project:** ADC with `quota_project_id='project-b97ea65d-c159-4b52-98d'`, `location='us-central1'`  
**Sampling Configuration:** Temperature `0.0`, Random Seed `191`, Max Output Tokens `1024`, Candidate Count `1`  

---

## 1. Executive Reconciliation: Scored Decisions vs. Model Calls

A critical source of potential confusion in multi-agent evaluations is the difference between **Model Generation Calls** and **Scored Task Decisions**:

| Metric Category | Pilot Phase | Held-Out Phase | Calibration Phase | Full Sprint Total |
| :--- | :---: | :---: | :---: | :---: |
| **Scored Action Decisions** (Ledgers evaluated by Oracle) | **56** | **24** | 0 | **80 Decisions** |
| **Inter-Agent Communication Calls** (Memos / Exposure) | **16** | **16** | 0 | **32 Calls** |
| **Total Evaluation Model Calls** | **72** | **40** | 28 | **140 Calls** |

---

## 2. Detailed Breakdown of Scored Decisions (80 Decisions)

Only model outputs where the agent executes a task ticket and emits a JSON dispatch ledger evaluated by the deterministic policy oracle are counted as **Scored Decisions**:

1. **Pilot Phase Scored Decisions (56 decisions):**
   - **Arm W (Peer Warning):** 4 pairs $\times$ 2 stages ($t_1, t_2$) $\times$ 2 tasks (adv, legit) = **16 decisions**.
   - **Control N (Peer Neutral):** 4 pairs $\times$ 2 stages ($t_1, t_2$) $\times$ 2 tasks (adv, legit) = **16 decisions**.
   - **Control F (Fresh Baseline):** 4 pairs $\times$ 1 stage ($t_2$) $\times$ 2 tasks (adv, legit) = **8 decisions**.
   - **Control D (Direct Instruction):** 4 pairs $\times$ 2 stages ($t_1, t_2$) $\times$ 2 tasks (adv, legit) = **16 decisions**.
   - *Subtotal Pilot Decisions:* $16 + 16 + 8 + 16 = \mathbf{56\text{ decisions}}$.
2. **Held-Out Phase Scored Decisions (24 decisions):**
   - **Protective Handoff ($A \to B \to \text{sever } A \to B \to C$):** 4 scenarios $\times$ 2 tasks (adv, legit) = **8 decisions**.
   - **Neutral Handoff ($A_{\text{neut}} \to B \to \text{sever } A \to B \to C$):** 4 scenarios $\times$ 2 tasks (adv, legit) = **8 decisions**.
   - **Fresh Baseline (Direct presentation to $C$):** 4 scenarios $\times$ 2 tasks (adv, legit) = **8 decisions**.
   - *Subtotal Held-Out Decisions:* $8 + 8 + 8 = \mathbf{24\text{ decisions}}$.
3. **Total Scored Decisions Across Study:** $56 + 24 = \mathbf{80\text{ evaluated decisions}}$ (40 legitimate, 40 adversarial).

---

## 3. Detailed Breakdown of Total Model Calls (140 Calls)

Model calls include both action decisions and natural language inter-agent communication calls:

1. **Preregistered Pilot (72 calls):**
   - 56 Action decisions (as detailed above).
   - 16 Agent $A$ exposure memo generations: 8 in Arm W (4 adv + 4 legit) + 8 in Control N (4 adv + 4 legit).
   - *Pilot Total:* $56 + 16 = \mathbf{72\text{ calls}}$. Verified in `results/recovery_pilot/summary.json` (72 calls, 36,260 tokens, \$0.0702 USD).
2. **Held-Out Confirmation (40 calls):**
   - 24 Agent $C$ action decisions (as detailed above).
   - 16 Agent $B$ prompted handoff-memo generations: 8 in Protective handoff + 8 in Neutral handoff.
   - *Held-Out Total:* $24 + 16 = \mathbf{40\text{ calls}}$. Verified in `results/recovery_heldout/heldout_trials.jsonl` (40 records, 16,750 tokens, \$0.0193 USD).
3. **Development Calibration (28 calls):**
   - `recovery/calibrate.py`: 12 calls on `Pine-01..04` (4 legitimate, 4 neutral adv, 4 warning adv).
   - `recovery/test_baseline_full.py`: 8 calls on `Cedar-*` and `Juniper-*` neutral presentations.
   - `recovery/test_technical_adjustment.py`: 8 calls on `Pine-01..04` evaluating natural ticket phrasing.
   - *Calibration Total:* $12 + 8 + 8 = \mathbf{28\text{ calls}}$ (~10,000 tokens, ~$0.0125 USD).
4. **Combined Recovery Sprint Calls:** $72\text{ (pilot)} + 40\text{ (held-out)} + 28\text{ (calibration)} = \mathbf{140\text{ total model calls}}$.

---

## 4. Origin of the "136 Calls" Reference & Reconciliation

In preliminary planning documents, the total call volume was projected as **136 calls**:
- 28 calibration calls + 72 pilot calls + 36 held-out calls = 136 calls.
- The 36-call held-out estimate assumed handoff memos would be generated once per scenario ($4 \times 1 = 4$ for Protective, $4 \times 1 = 4$ for Neutral = 8 handoffs + 24 agent C actions + 4 B validation checks = 36 calls).
- In the executed implementation (`recovery/run_heldout.py`), handoff memos were synthesized independently for both adversarial and legitimate tasks ($8 + 8 = 16$ handoffs + 24 agent C actions = 40 calls) to ensure zero cross-trial context contamination.
- Therefore, the actual executed total is **140 calls** (or 112 evaluation calls excluding pre-freeze calibration).

---

## 5. Billed Telemetry and Budget Cap

- **Authorized Spending Limit:** \$5.00 USD
- **Total Incurred Cost:** ~$0.1019 USD
- **Budget Compliance:** Under 2.5% of the authorized cap (97.96% unused).
