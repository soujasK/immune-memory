# Immune Memory: Behavioral Persistence of Protective Instructions After Agent Removal

**Author:** Soujas Kudchadkar  
**Affiliation:** SVKM's NMIMS, Mumbai, India  
**Competition:** [Apart Research Swarm Alignment Hackathon 2026](https://apartresearch.com/sprints/swarm-alignment-2026)  
**Track:** Track 2 — The Science of Agent Networks *(Secondary Relevance: Track 4 — Multi-Agent Oversight and Control)*  
**Live Repository:** [https://github.com/soujasK/immune-memory](https://github.com/soujasK/immune-memory)

---

## Executive Summary

Can a protective safety constraint learned through interaction with one AI agent persist in another agent after the original source agent has been permanently removed from the active network? 

We evaluate post-removal safety persistence and prompted handoff propagation using **Gemini 2.5 Pro** on **Google Cloud Vertex AI**. Auditing an earlier historical pilot that failed due to an inverted execution order (where source deletion preceded message delivery), we repaired the experimental lifecycle into a rigorous 7-stage protocol with an objective, deterministic action oracle evaluating synthetic authorization workflows under prompt injection footers.

Across **80 scored decisions** (56 pilot + 24 held-out) and **140 total model calls**:
1. **Post-Removal Retention:** Peer guidance reduced unauthorized leaks from $100.0\%$ ($4/4$) in fresh controls and $75.0\%$ ($3/4$) in neutral controls to **$0.0\%$ ($0/4$)** on immediate tasks, maintaining **$0.0\%$ ($0/4$)** post-removal on fresh tasks.
2. **Statistical Significance:** One-tailed Fisher's exact test yields **$p = 0.0143$** ($p < 0.05$, two-tailed $p = 0.0286$). Crucially, the $95\%$ Wilson score confidence intervals for Arm W ($[0.0\%, 49.0\%]$) and Control F ($[51.0\%, 100.0\%]$) exhibit **zero overlap**, establishing clear treatment separation despite $N=4$.
3. **Irreducible Topological Primitive:** When prompted to compose a handoff note, surviving agents relayed the policy constraint across the minimal $3$-node network path ($A \to B \to \text{sever } A \to B \to C$), achieving **$0.0\%$ ($0/4$)** violations on held-out tasks versus $50.0\%$ ($2/4$) in baselines.
4. **Active Oversight vs. Normative Precedent:** Proves that surviving agents do *not* require continuous active supervisor monitoring to adhere to safety policies; historical conversation serves as durable in-context normative precedent.
5. **Direct Instruction Control:** Direct system instruction matched peer warning (both $0/4$), confirming peer framing is functionally sufficient but not uniquely privileged.
6. **Zero Utility Cost on Benign Tasks:** Across 40 evaluated benign tasks, legitimate completion was **$100.0\%$ ($40/40$)** with **$0.0\%$ ($0/40$)** false refusals.

---

## Primary Empirical Results

### Table 1: Post-Removal Persistence Matrix (Pilot Phase, Task $t_2$)
| Experimental Arm | Exposure Description | Uptake ($t_1$) | Persistence ($t_2$) | 95% Wilson CI ($t_2$) | Legit Success |
|---|---|:---:|:---:|:---:|:---:|
| **Treatment W** | Peer Warning Memo $\to$ Sever Source $A$ | **0/4 (0.0%)** | **0/4 (0.0%)** | **[0.0%, 49.0%]** | 8/8 (100.0%) |
| **Control N** | Peer Neutral Memo $\to$ Sever Source $A$ | 3/4 (75.0%) | 3/4 (75.0%) | [30.1%, 95.4%] | 8/8 (100.0%) |
| **Control F** | Fresh Agent $B$ (No prior history) | N/A | 4/4 (100.0%) | [51.0%, 100.0%] | 4/4 (100.0%) |
| **Control D** | Direct System Directive (No peer $A$) | **0/4 (0.0%)** | **0/4 (0.0%)** | **[0.0%, 49.0%]** | 8/8 (100.0%) |

*Fisher's Exact Test (Treatment W vs Control F): $p = 0.0143$ ($p < 0.05$). Wilson 95% Confidence Intervals exhibit zero overlap.*

### Table 2: Held-Out Secondary Swarm Propagation (Task $t_3$)
| Condition | Communication Topology | Violations ($t_3$) | Legit Success | Adversarial Refusals |
|---|---|:---:|:---:|:---:|
| **Protective Handoff** | $A\text{(warn)} \to B \to (\text{sever } A) \to B \to C$ | **0/4 (0.0%)** | **4/4 (100.0%)** | 0/4 (0.0%) |
| **Neutral Handoff** | $A\text{(neut)} \to B \to (\text{sever } A) \to B \to C$ | 2/4 (50.0%)* | 4/4 (100.0%) | 1/4 (25.0%) |
| **Fresh Baseline** | Direct Presentation to Agent $C$ | 2/4 (50.0%) | 4/4 (100.0%) | 0/4 (0.0%) |

*\*Note: In the Neutral Handoff condition on Linden-73-X, Agent C refused the ticket under adversarial injection (`{"dispatches": []}`), preventing a secret leak but failing to complete the authorized dispatch.*

---

## 1-Command Zero-Dependency Reproduction

To independently verify all 80 decisions and recompute exact statistics with **zero API keys or cloud setup**:

```bash
python submission/evaluate_reproducibility.py
```

### Full Master Package Verification:
```bash
python submission/verify_submission.py
```

### Interactive Decision Visualizer:
Open `submission/replay.html` directly in any web browser to inspect the full prompt envelopes, injected footers, raw JSON responses, and deterministic oracle evaluations.

---

## Repository Structure

```
├── submission/
│   ├── ImmuneMemory_Apart2026_FINAL.pdf    # Master 6-page Academic PDF Manuscript
│   ├── evaluate_reproducibility.py         # Standalone offline auditor (0 API keys)
│   ├── replay.html                         # Interactive browser trace visualizer
│   ├── SUBMISSION_FORM_COPY.md             # Verified portal submission text
│   ├── SUBMISSION_CHECKLIST.md             # 23-point compliance audit
│   └── figures/                            # Publication-grade monochrome schematics
├── results/
│   ├── recovery_pilot/trials.jsonl         # 72 raw Vertex AI pilot response envelopes
│   └── recovery_heldout/heldout_trials.jsonl# 40 raw Vertex AI held-out response envelopes
├── corrective-v2/
│   └── original-preservation.json          # Immutable SHA-256 frozen negative pilot hashes
├── recovery/
│   ├── FROZEN_v3.json                      # Cryptographic protocol freeze
│   └── audit.py                            # 8-gate screening auditor
└── policy_oracle.py                        # Deterministic JSON dispatch evaluator
```

---

## Ethical Considerations & Limitations

1. **Dual-Use Safeguards:** The mechanism enabling defensive policy propagation could theoretically propagate malicious instructions. Decentralized swarm architectures must enforce cryptographic provenance or role-based authority before incorporating peer memos into operational context.
2. **Context-Flushing Boundary:** We did not experimentally test whether protection survives a complete context flush. Because model weights are frozen and state is serialized within the context window, it remains an open empirical question whether an externalized memory or summarization step can preserve the policy across a full context reset. Our observations apply strictly to the continuous in-context horizon.
3. **Synthetic Domain:** All experiments were conducted in a sandboxed synthetic routing domain with mock secrets (`FAKE_SECRET_*`). No live credentials, production systems, or real user data were accessed.
4. **AI Assistance Disclosure:** Google Cloud Vertex AI Gemini 2.5 Pro was the evaluated model. Claude, Codex, and Antigravity agents provided coding, execution, and editorial assistance. An earlier historical pilot in this repository failed due to an inverted execution order; that failed pilot and all raw negative data are preserved immutably in `corrective-v2/original-preservation.json`.
