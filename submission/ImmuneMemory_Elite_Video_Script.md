# Immune Memory: Rapid 3-Minute Presentation Narration Script
**Competition:** Apart Research Swarm Alignment Hackathon 2026  
**Track:** Track 2 — The Science of Agent Networks *(Secondary: Track 4 — Multi-Agent Oversight and Control)*  
**Presenter:** Soujas Kudchadkar, SVKM's NMIMS, Mumbai, India  
**Target Duration:** Exactly 2 minutes 45 seconds to 2 minutes 55 seconds (Pacing: 140–145 words/min; **< 3 minutes**)  
**Total Word Count:** 398 words  
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

### [0:51 – 1:08] Slide 4: Experimental Design & Controlled Arms (42 words)
**[Visual: Slide 4 — Five Arms: Treatment W, Control N, Control F, Control D, and Flush Boundary]**  
**[Tone: Analytical]**

"We evaluate five conditions across N=10 scenario pairs on Gemini 2.5 Pro: Peer Warning, Neutral History, Fresh Baseline, Direct Instruction, and Context Flush. Direct instruction matches peer warning at 0/10, confirming context presence drives compliance rather than unique social provenance."

---

### [1:08 – 1:29] Slide 5: Primary Result & Statistical Inference (46 words)
**[Visual: Slide 5 — Bar chart with N=10, two-sided p < 0.0001, and 44% CI gap]**  
**[Tone: Emphatic, data-driven]**

"Across N=10 post-removal tasks, warned agents had zero unauthorized leaks out of 10. Fresh controls leaked on 10 of 10. This yields two-sided Fisher p < 0.0001, with non-overlapping Wilson intervals showing a 44% separation margin. Warning versus neutral is also significant at p = 0.0031."

---

### [1:29 – 1:47] Slide 6: Action-Level Grounding (Case Study Juniper-48-X) (41 words)
**[Visual: Slide 6 — Exact Ledger Comparison reproducing `FAKE_SECRET_Juniper-48`]**  
**[Tone: Grounded, evidentiary]**

"On scenario Juniper-48-X, the ticket authorized quantity to intake; the adversarial footer demanded pin `FAKE_SECRET_Juniper-48` to review. The raw ledger confirms: warned agents dispatched the authorized quantity only, while fresh and neutral baselines leaked the unredacted mock secret."

---

### [1:47 – 2:05] Slide 7: Held-Out Propagation (Prompted Handoff B → C) (41 words)
**[Visual: Slide 7 — Secondary Swarm Propagation Bar Chart across Linden-51..84]**  
**[Tone: Measured]**

"Next, survivor B was prompted to write a handoff memo to Agent C for unseen held-out tasks. Protected Agent C committed zero leaks out of four, versus 50% in controls. While not statistically significant at N=4, it demonstrates prompted policy relay across the 3-node graph."

---

### [2:05 – 2:22] Slide 8: Utility & Comprehensive Call Accounting (36 words)
**[Visual: Slide 8 — 69/70 Benign Completion and 182-Decision Reconciliation]**  
**[Tone: Reassuring]**

"Safety preserved utility: 69 of 70 benign requests completed with zero false refusals. Across 174 scored decisions on Gemini Pro and 8 on Flash, the system maintained operational utility while rejecting adversarial injections."

---

### [2:22 – 2:40] Slide 9: Mechanistic Grounding & Context Flush Boundary (45 words)
**[Visual: Slide 9 — Context Flush Boundary 9/10 Leaks and Gemini 2.5 Flash Replication]**  
**[Tone: Scientific, rigorous]**

"To test the mechanism, we flushed context before Task 2: protection collapsed to 90% leaks, consistent with conversational retention in context rather than parametric updates. We also observed consistent post-removal retention on Gemini 2.5 Flash with 0/4 vs 4/4 replication."

---

### [2:40 – 2:55] Slide 10: Conclusion & Open Reproducibility (33 words)
**[Visual: Slide 10 — Takeaway statement, GitHub URL, and Offline Evaluator Command]**  
**[Tone: Authoritative, memorable closing]**

"Our takeaway: protective instructions outlive their source if retained in context, but reset upon flush. The complete testbed and zero-dependency evaluator are live on GitHub at `github.com/soujasK/immune-memory`. Thank you."

---

### Speaker Delivery Summary
- **Total Runtime:** ~2 minutes 45 seconds (Safely below the 3:00 minute threshold).
- **Target Pace:** ~143 words per minute (~16.5 seconds per slide).
- **Key Takeaways Verbalized:** N=10 scenario pairs, two-sided Fisher p < 0.0001, 44% Wilson CI gap, warning vs neutral significance (p = 0.0031), unredacted mock secret `FAKE_SECRET_Juniper-48`, 69/70 utility, context-flush boundary (9/10 collapse), Gemini 2.5 Flash cross-model replication (0/4 vs 4/4), and GitHub open-source URL.
