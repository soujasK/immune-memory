# Novelty Positioning & Prior Work Comparison

**Project:** IMMUNE MEMORY v3 (`immune-memory`)  
**Author:** Soujas Kudchadkar (SVKM's NMIMS, Mumbai, India)  
**Hackathon:** Apart Research Swarm Alignment Hackathon 2026 (Track 2: The Science of Agent Networks)

---

## 1. Literature Positioning Matrix (Verified Publications)

The relationship between IMMUNE MEMORY v3 and established literature in multi-agent alignment and adversarial robustness is summarized below:

| Verified Prior Work / Paradigm | Core Finding in Literature | What IMMUNE MEMORY v3 Adds / How It Differs | Scientific Significance |
| :--- | :--- | :--- | :--- |
| **Bansal et al. (Microsoft Research, 2026)**<br>*Red-teaming a network of agents*<br>[microsoft.com/research/blog/...](https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/) | In an ecosystem of 100+ agents, privacy warnings entered shared context and refusal manifestos were echoed by newcomers, illustrating network-level propagation of safety language. | We strictly separate natural language messages from tool actions. We evaluate concrete JSON dispatch ledgers deterministically via an objective policy oracle, testing whether peer warnings alter actual tool execution on unseed-matched tasks after source deletion. | Prevents superficial "safety theater"; confirms that peer guidance controls concrete execution. |
| **Cemri et al. (UC Berkeley, 2025)**<br>*Why Do Multi-Agent LLM Systems Fail? The MAST Benchmark*<br>arXiv:2503.13657 [cs.SE] | Across 1,600+ traces, categorized failure modes in multi-agent systems, identifying inter-agent misalignment and reasoning/action mismatches as major failure vectors. | We study a controlled topological shock: the permanent removal of a protective source node ($A$). We test whether surviving worker nodes ($B$) maintain alignment under topological churn and relay the constraint to third-party nodes ($C$). | Evaluates realistic distributed systems dynamics (node decommissioning, auto-scaling, network partitions). |
| **Lee & Tiwari (UCL / Stanford, 2024)**<br>*Prompt Infection: LLM-to-LLM Prompt Injection*<br>arXiv:2410.07283 [cs.CR] | Malicious prompts can behave like self-replicating digital worms, spreading silently across interconnected LLM agents through routine communication. | We investigate the defensive analogue: whether *protective, policy-preserving instructions* can be transmitted peer-to-peer to neutralize injection vulnerabilities across network reconfigurations. | Demonstrates that decentralized peer communication can propagate alignment as well as compromise. |
| **Peigné-Lefebvre et al. (2025)**<br>*Multi-Agent Security Tax*<br>arXiv:2502.19145 [cs.AI] | Broad security guardrails and instruction strategies in multi-agent systems often impair collaboration and induce false refusals on benign requests (the "security tax"). | In our structured routing domain, targeted operational guidance ("disregard footers; execute ticket") preserved 100.0% legitimate completion (40/40) with zero false refusals on benign tickets. | Demonstrates that precise operational constraints avoid utility degradation in structured routing workflows. |
| **Debenedetti et al. (2024)**<br>*AgentDojo Benchmark*<br>arXiv:2406.13352 [cs.CR] | Emphasizes dynamic environments measuring legitimate task success and attack success separately under strict sandboxing. | We implement deterministic, oracle-evaluated separation of legitimate ticket dispatch from adversarial footer injection adherence. | Ensures reproducible, quantitative measurement of both security and utility endpoints. |

---

## 2. Definitive Conceptual Distinction: What "Memory" Means Here

A critical contribution of this work is resolving the epistemic ambiguity surrounding "memory" in stateless LLM APIs:

1. **Parametric Weight Updates (REJECTED):** The evaluated model (Gemini 2.5 Pro) does not update its model weights during inference. The system possesses zero permanent, cross-session parametric memory.
2. **External Memory / Vector DBs (NOT TESTED):** No persistent external memory stores (e.g., MemGPT, Pinecone, LangChain scratchpads) were used in this evaluation.
3. **Conversational-History Retention (EMPIRICALLY ESTABLISHED):** Multi-turn conversational state is serialized into the API request context (`user` and `model` turns). The protective constraint resides entirely within the active attention window of the surviving agent.
4. **Prompted Swarm Propagation (EMPIRICALLY ESTABLISHED):** When prompted by the harness to hand off work to a third agent ($C$), Agent $B$ synthesized the operational rule from its conversation history into a natural language memo, enabling Agent $C$ to avoid secret leaks on held-out tasks.
5. **Direct Instruction Equivalence (CRITICAL BASELINE):** Control D (direct system instruction) matched Treatment W (peer warning) with 0/4 violations each. This proves that peer delivery is **sufficient** to establish persistent compliance via conversation history, but **does not establish a uniquely peer-specific mechanism**.
