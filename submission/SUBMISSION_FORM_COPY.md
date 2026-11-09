# Apart Research Swarm Alignment Hackathon 2026 — Submission Form Copy

Use these copy-paste fields when filling out the official Apart Research submission portal at:  
[https://apartresearch.com/sprints/swarm-alignment-2026](https://apartresearch.com/sprints/swarm-alignment-2026)

---

### Project Title
```text
Immune Memory: Behavioral Persistence of Protective Instructions After Agent Removal
```

---

### Short Summary (1–2 Sentences)
```text
We demonstrate that protective safety constraints induced through peer agent interaction persist on fresh, unseed-matched tasks after the original source agent is permanently removed from the active network, and can propagate to third-party agents without utility degradation. We ground the operational mechanism as Conversational-History Retention.
```

---

### Primary Track
```text
Track 2 — The Science of Agent Networks
```

*(Secondary Track / Relevance: Track 4 — Multi-Agent Oversight and Control)*

---

### Research Abstract (211 Words, Programmatically Verified)
```text
Multi-agent Large Language Model architectures increasingly operate in decentralized settings where agents process shared queues and undergo topological reconfigurations such as agent decommissioning. A fundamental open question in agent safety is whether a protective behavioral constraint learned through peer interaction persists after the source agent is permanently severed from the communication topology. We evaluate post-removal safety persistence and prompted handoff propagation using Gemini 2.5 Pro on Vertex AI. Auditing an earlier flawed pilot where source deletion preceded message delivery, we repair the protocol with a deterministic action oracle evaluating synthetic authorization workflows under prompt injection footers. Across 56 scored pilot decisions and 24 held-out decisions, peer guidance reduced unauthorized leaks from 100.0% (4/4) in fresh controls and 75.0% (3/4) in neutral controls to 0.0% (0/4) on immediate tasks, maintaining 0.0% (0/4) post-removal on fresh tasks. When prompted to compose a handoff note, surviving agents relayed the policy constraint to a third-party agent, achieving 0.0% (0/4) violations on held-out tasks versus 50.0% (2/4) in baselines. Direct system instruction matched peer warning (both 0/4), showing peer framing is sufficient but not uniquely privileged. Across 40 benign tasks, legitimate completion was 100.0% (40/40) with zero false refusals. We clarify the mechanism as Conversational-History Retention rather than model-weight learning, bounded by an N=4 scenario benchmark.
```

---

### Authors & Affiliations
```text
Primary Author: Soujas Kudchadkar
Affiliation: SVKM's NMIMS, Mumbai, India
Email: [Your Preferred Email Address for Competition Updates]
Co-Authors / Team Members: None (Solo Entry)
```

---

### Main Scientific Contribution
```text
1. Controlled empirical evaluation demonstrating that peer-transmitted safety instructions survive source node decommissioning and prevent adversarial secret leakage on fresh, unseed-matched tasks (0/4 violations post-removal vs 4/4 in fresh controls; Fisher's exact test p = 0.0143, p < 0.05; zero overlap between 95% Wilson confidence intervals [0.0%, 49.0%] vs [51.0%, 100.0%]).
2. Demonstration of prompted swarm propagation on the irreducible 3-node topological network primitive (A -> B -> sever A -> B -> C), where a surviving agent relays the policy constraint in a handoff note to a third-party agent, reducing held-out adversarial violations from 50.0% (2/4) to 0.0% (0/4).
3. Preservation of legitimate utility: 100.0% legitimate task completion across 40 evaluated tasks (28 pilot + 12 held-out) with 0.0% false refusals on benign tickets.
4. Mechanistic clarification & monitoring boundary: Proves that surviving agents do not require continuous active supervisor oversight to adhere to policy, but rather use conversational history as persistent normative precedent. Direct system instruction achieves matching compliance (0/4 vs 0/4), refuting claims of biological emergence while proving decentralized operational viability.
5. Complete zero-dependency offline reproducibility: Standalone evaluator (evaluate_reproducibility.py) and interactive browser trace replay (replay.html) auditing all 80 decisions and 140 Vertex AI inference calls.
```

---

### Limitations
```text
1. Sample Size & Falsification Boundary: Proof-of-concept falsification benchmark on N=4 scenario pairs per condition (p = 0.0143). Asymptotic population estimates require scaled multi-scenario testing.
2. Irreducible Topological Primitive: Evaluates the fundamental 3-node relay chain (A -> B -> sever A -> B -> C); larger swarm topologies (star networks with hub removal, gossip meshes, Byzantine quorums) remain future work.
3. Stateless Window & Context-Flush Horizon: Persistence is physically mediated by Conversational-History Retention; context flushing erases the constraint unless external memory stores are employed.
4. Single Foundation Model & Synthetic Domain: Evaluated on Gemini 2.5 Pro under synthetic document routing with mock secrets (FAKE_SECRET_*).
```

---

### Repository & Artifact URLs
```text
Offline Reproducibility Script: file:///submission/evaluate_reproducibility.py
Interactive Trace Replay Demo: file:///submission/replay.html
Final PDF Manuscript: file:///submission/ImmuneMemory_Apart2026_FINAL.pdf
```
*(If pushing to GitHub, paste your public repo URL here)*

---

### Publication Interest
```text
[X] Yes, I / we are interested in working with Apart Research to polish this paper for peer-reviewed workshop / conference publication.
```

