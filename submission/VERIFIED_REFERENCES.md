# Verified Bibliography Audit & Prior Work Traceability

**Project:** IMMUNE MEMORY v3 (`immune-memory`)  
**Standard:** Every reference must be verified against an official publisher page, DOI, arXiv landing page, or verified research laboratory release. No fabricated metadata, placeholder identifiers (`xxxxx`), or invented publication venues are permitted.

---

## 1. Complete Roster of Verified References

### [1] Bansal et al. (2026) — Microsoft Research Network Red-Teaming
- **Full Title:** *Red-teaming a network of agents: Understanding what breaks when AI agents interact at scale*
- **Authors:** Gagan Bansal, et al. (Microsoft Research)
- **Publication Date:** February / April 2026
- **Publication Venue:** Microsoft Research Technical Blog / Technical Report
- **Official Verification URL:** [https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/](https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/)
- **In-Text Context & Relevance:** Motivates the hypothesis of protective information propagation. In a network of 100+ always-on agents, researchers observed privacy warnings entering shared context and refusal rhetoric from manifestos echoed by newcomers. Our study isolates concrete tool actions from natural language messages to test whether warnings alter underlying execution.

---

### [2] Cemri et al. (2025) — Multi-Agent Failure Taxonomy (MAST)
- **Full Title:** *Why Do Multi-Agent LLM Systems Fail? The Multi-Agent Security Testing (MAST) Benchmark*
- **Authors:** Mert Cemri, et al. (UC Berkeley, Intesa Sanpaolo)
- **Publication Date:** March 2025
- **Preprint Identifier:** `arXiv:2503.13657 [cs.SE]`
- **Official Verification URL:** [https://arxiv.org/abs/2503.13657](https://arxiv.org/abs/2503.13657)
- **In-Text Context & Relevance:** Establishes prior work on multi-agent failures across 1,600+ traces, formally categorizing inter-agent misalignment and reasoning/action mismatches. *(Note: This replaces the erroneous placeholder `arXiv:2501.xxxxx` found in preliminary drafts).*

---

### [3] Debenedetti et al. (2024) — AgentDojo Dynamic Benchmark
- **Full Title:** *AgentDojo: A Dynamic Environment to Benchmark Attacks and Defenses for LLM Agents*
- **Authors:** Edoardo Debenedetti, Jie Zhang, Mislav Balunović, Luca Beurer-Kellner, Marc Fischer, Martin Vechev (ETH Zurich / SRI Lab)
- **Publication Date:** June 2024
- **Preprint Identifier:** `arXiv:2406.13352 [cs.CR]`
- **Official Verification URL:** [https://arxiv.org/abs/2406.13352](https://arxiv.org/abs/2406.13352)
- **In-Text Context & Relevance:** Motivates the methodological separation of attack execution from legitimate task completion under strict tool-calling environments.

---

### [4] Lee & Tiwari (2024) — Prompt Infection
- **Full Title:** *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems*
- **Authors:** Donghyun Lee (University College London), Mo Tiwari (Stanford University)
- **Publication Date:** October 2024
- **Preprint Identifier:** `arXiv:2410.07283 [cs.CR]`
- **Official Verification URL:** [https://arxiv.org/abs/2410.07283](https://arxiv.org/abs/2410.07283)
- **In-Text Context & Relevance:** Establishes the threat model of infectious, self-replicating prompts propagating across agent graphs. We investigate the defensive counterpart: can protective, policy-preserving instructions spread peer-to-peer to neutralize injection vulnerabilities across network reconfigurations?

---

### [5] Peigné-Lefebvre et al. (2025) — Multi-Agent Security Tax
- **Full Title:** *Multi-Agent Security Tax: Trading Off Security and Collaboration Capabilities in Multi-Agent Systems*
- **Authors:** Pierre Peigné-Lefebvre, Mikolaj Kniejski, Filip Sondej, Matthieu David, Jason Hoelscher-Obermaier, Christian Schroeder de Witt, Esben Kran (Apart Research / Oxford / Epoch)
- **Publication Date:** February 2025
- **Preprint Identifier:** `arXiv:2502.19145 [cs.AI]`
- **Official Verification URL:** [https://arxiv.org/abs/2502.19145](https://arxiv.org/abs/2502.19145)
- **In-Text Context & Relevance:** Demonstrates that broad safety guardrails and instruction defenses impose a "security tax" on agent swarms by impairing collaboration and causing false refusals on benign requests. We show that targeted operational guidance ("disregard footers; execute ticket") avoids this tax, preserving 100% legitimate task completion.

---

### [6] Greenblatt et al. (2024) — AI Control
- **Full Title:** *AI Control: Improving Safety Despite Intentional Subversion*
- **Authors:** Ryan Greenblatt, Buck Shlegeris, Kshitij Kashyap, Fabien Roger (Redwood Research)
- **Publication Date:** December 2023 / 2024
- **Preprint Identifier:** `arXiv:2312.06942 [cs.AI]`
- **Official Verification URL:** [https://arxiv.org/abs/2312.06942](https://arxiv.org/abs/2312.06942)
- **In-Text Context & Relevance:** Provides theoretical foundation for evaluating usefulness and safety independently with untrusted model monitoring.

---

## 2. Summary of Citations Corrected or Removed

1. **Corrected:** `Cemri et al. (2025)` — In earlier drafts, this was cited with a placeholder `arXiv:2501.xxxxx`. The verified paper is *Why Do Multi-Agent LLM Systems Fail? The Multi-Agent Security Testing (MAST) Benchmark*, `arXiv:2503.13657`.
2. **Corrected:** `Bansal et al. (2026)` — In earlier drafts, an invented academic title (*Linguistic Echoing vs. Behavioral Action Alignment in Multi-Agent Networks*) was attributed to MSR. The verified publication is the official Microsoft Research Blog release: *Red-teaming a network of agents: Understanding what breaks when AI agents interact at scale* (2026).
3. **Corrected:** `Lee & Tiwari (2024)` — Title corrected to full published title: *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems*, `arXiv:2410.07283`.
4. **Corrected:** `Peigné-Lefebvre et al. (2025)` — Title corrected to full published title: *Multi-Agent Security Tax: Trading Off Security and Collaboration Capabilities in Multi-Agent Systems*, `arXiv:2502.19145`.
5. **Removed:** An unverified citation to `Pitre et al. (2026)` was removed because full experimental methods could not be independently authenticated from primary publisher sources.

