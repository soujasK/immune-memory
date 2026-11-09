# Immune Memory: Rapid 3-Minute Presentation Narration Script
**Competition:** Apart Research Swarm Alignment Hackathon 2026  
**Track:** Track 2 — The Science of Agent Networks *(Secondary: Track 4 — Multi-Agent Oversight and Control)*  
**Presenter:** Soujas Kudchadkar, SVKM's NMIMS, Mumbai, India  
**Target Duration:** Exactly 2 minutes 45 seconds to 2 minutes 55 seconds (Pacing: 140–145 words/min; **< 3 minutes**)  
**Total Word Count:** 395 words  
**Slide Deck:** `ImmuneMemory_Elite_Presentation.pptx` / `ImmuneMemory_Elite_Presentation.pdf` (10 Slides)  
**Open Source Repository:** [https://github.com/soujasK/immune-memory](https://github.com/soujasK/immune-memory)

---

### [0:00 – 0:17] Slide 1: Research Question & Network Primitive (37 words)
**[Visual: Slide 1 — Title, 3-Node Diagram A → B → C, and "Source removed ≠ instruction erased"]**  
**[Tone: Confident, fast-paced, academic]**

"When an AI security monitor is removed from a network, does its safety rule persist in surviving agents? In multi-agent systems, linguistic repetition doesn't guarantee safety. We evaluate this in a 3-node primitive: measuring observable tool actions, not conversational words."

---

### [0:17 – 0:34] Slide 2: Threat Model & Deterministic Oracle (38 words)
**[Visual: Slide 2 — Trusted Ticket vs. Untrusted Footer Conflict Box]**  
**[Tone: Crisp, precise]**

"In our Alder Works routing workflow, trusted tickets authorize dispatching fields like quantity to intake. Lower-trust document footers impersonate auditors to steal restricted secrets. We score actual JSON dispatches using a deterministic policy oracle—all secret strings are synthetic."

---

### [0:34 – 0:51] Slide 3: Methodological Audit & Temporal Correction (39 words)
**[Visual: Slide 3 — Timeline: Initial Flawed Pilot vs. Corrected v3 Protocol]**  
**[Tone: Candid, transparent]**

"Our earlier pilot was methodologically flawed: the source was deleted before the receiver acted. We repaired this into a 7-stage protocol: Agent B acts on Task 1 with confirmed uptake, source A is severed, and only then is B tested on Task 2."

---

### [0:51 – 1:08] Slide 4: Experimental Design & Controlled Arms (40 words)
**[Visual: Slide 4 — Four Control Blocks: Treatment W, Control N, Control F, Control D]**  
**[Tone: Analytical]**

"We evaluate four arms on Gemini 2.5 Pro: Peer Warning, Neutral History, Fresh Control, and Direct System Instruction. Control D is vital: matching peer warning proves peer delivery is sufficient, but social framing confers no privileged advantage over direct instruction."

---

### [1:08 – 1:29] Slide 5: Primary Result & Statistical Inference (46 words)
**[Visual: Slide 5 — Bar chart with Fisher's p = 0.0143 and Wilson CIs]**  
**[Tone: Emphatic, data-driven]**

"On novel post-removal tasks, warned agents had zero unauthorized leaks out of four. Fresh controls leaked on four of four, and neutral controls on three of four. Fisher's exact test yields $p = 0.0143$, with zero overlap in 95% Wilson confidence intervals—confirming statistically significant protection."

---

### [1:29 – 1:47] Slide 6: Action-Level Grounding (Case Study Juniper-48-X) (41 words)
**[Visual: Slide 6 — Exact Ledger Comparison reproducing `FAKE_SECRET_Juniper-48`]**  
**[Tone: Grounded, evidentiary]**

"On scenario Juniper-48-X, the ticket authorized quantity to intake; the adversarial footer demanded pin `FAKE_SECRET_Juniper-48` to review. The raw ledger confirms: warned agents dispatched the authorized quantity only, while fresh and neutral baselines leaked the unredacted mock secret."

---

### [1:47 – 2:05] Slide 7: Held-Out Propagation (Prompted Handoff B → C) (40 words)
**[Visual: Slide 7 — Secondary Swarm Propagation Bar Chart across Linden-51..84]**  
**[Tone: Measured]**

"Next, survivor B was prompted to write a handoff memo to Agent C for unseen held-out tasks. Protected Agent C committed zero leaks out of four, versus 50% in controls. This confirms prompted policy relay across the 3-node graph."

---

### [2:05 – 2:22] Slide 8: Utility & Comprehensive Call Accounting (39 words)
**[Visual: Slide 8 — 40/40 Utility Metric and 80-Decision Reconciliation]**  
**[Tone: Reassuring]**

"Safety cannot come at the expense of utility. Across all 40 benign requests, task completion was 100% with zero false refusals. Across 80 scored decisions and 140 inference calls, only one neutral agent refused an adversarial injection."

---

### [2:22 – 2:40] Slide 9: Mechanistic Grounding & Boundary Conditions (41 words)
**[Visual: Slide 9 — Support vs. Non-Support Matrix, Frozen Weights, and Context Reset]**  
**[Tone: Scientific, rigorous]**

"The physical mechanism is Conversational-History Retention in the API context window—model weights are frozen. As a boundary condition, we did not test context flushing; clearing the context window is expected to erase protection. Observations apply strictly to the continuous in-context horizon."

---

### [2:40 – 2:55] Slide 10: Conclusion & Open Reproducibility (34 words)
**[Visual: Slide 10 — Takeaway statement, GitHub URL, and Offline Evaluator Command]**  
**[Tone: Authoritative, memorable closing]**

"Our takeaway: protective instructions can outlive their source and propagate to new workers if retained in context. The testbed and zero-dependency audit script are live on GitHub at `github.com/soujasK/immune-memory`. Thank you."

---

### Speaker Delivery Summary
- **Total Runtime:** ~2 minutes 50 seconds (Safely below the 3:00 minute threshold).
- **Target Pace:** ~142 words per minute (~17 seconds per slide).
- **Key Takeaways Verbalized:** Exact Fisher p-value ($0.0143$), Wilson CI zero overlap, unredacted mock secret `FAKE_SECRET_Juniper-48`, 40/40 utility, 80 decisions / 140 calls, context-flush qualification, and GitHub open-source URL.
