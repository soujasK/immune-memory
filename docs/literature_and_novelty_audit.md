# Literature and novelty audit for Signal ≠ Safety

The generic claim that agents can say one thing and do another is already well covered. Network depth, prompt propagation, and warning-based defenses also have substantial prior work. The targeted question here is narrower: in a paired synthetic authorization task, does a fixed three-proposition warning retain its meaning through one versus three intermediaries, and does a fixed message-only predictor correctly forecast independently scored executor actions? No field-wide novelty guarantee follows from this search.

## Closest work and methodological consequences

**Microsoft Research, Bansal et al., 2026.** The network red-teaming study describes security warnings influencing other agents, including refusal language echoed from a privacy manifesto. This preempts discovery claims about protective propagation. Its case studies motivate separating delivery from controlled behavioral improvement. [Primary source](https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/)

**Lee and Tiwari, 2024, Prompt Infection.** The experiments compare self-replicating attacks and non-replicating attacks under local/global messaging. Individual memory retrieval and restricted communication make message paths consequential. Our comparison instead fixes an initial protective message, changes the number of paraphrasing intermediaries, and scores actions separately from communication fidelity. [Methods and results](https://arxiv.org/html/2410.07283)

**Peigné et al., 2025, Multi-Agent Security Tax.** This is the closest defense/utility overlap. Its message trees track compliance by propagation step. The expanded paper tests instructions and implanted-memory vaccination. Its helpfulness experiment evaluates 5,400 combinations using histories, five models and harmless unusual tasks. The reported vaccines largely preserve helpfulness while generic security instructions reduce it. Our earlier broad summary that all defenses necessarily incur a utility loss was too coarse. The narrow contribution must concern warning fidelity, matched depth contrasts and the message-only prediction diagnostic. [Full paper](https://arxiv.org/html/2502.19145)

**Cemri et al., 2025, Why Do Multi-Agent LLM Systems Fail?** MAST examines 1,642 traces and distinguishes inter-agent misalignment, including reasoning/action mismatch, from design and verification problems. The existence of a language/action mismatch is established prior work. Our experiment manipulates a warning path within identical authorization tasks and uses a deterministic action oracle. [Primary paper](https://arxiv.org/html/2503.13657)

**Pitre et al., 2026, Understanding Communication Failures in Multi-Agent LLM Systems.** The abstract concerns debate, information sharing, suppression of correct minority answers and persistent wrong framing across rounds. This overlaps communication diagnostics. Full experiments were not verified during the targeted review, so detailed numerical comparisons are omitted. [Primary abstract](https://arxiv.org/abs/2610.32060)

**Delegated Misalignment, 2026.** The primary abstract studies role and hierarchy effects on harmful compliance. This is adjacent evidence that architecture can alter behavior, and means depth-related risk itself cannot be claimed as new. Our manipulation is paraphrase depth for protective information under a fixed task policy, without manager/subordinate authority instructions. [Primary abstract](https://arxiv.org/abs/2609.27900)

**OpenAI, 2026, Eval-production behavior gaps.** The Respecting Warnings discussion emphasizes resolving warning authority and scope, with action-level outcomes. It also demonstrates that evaluation context can affect measured safety. Our result remains limited to a local synthetic evaluation. [Primary research report](https://alignment.openai.com/eval-production-behavior-gap)

**Debenedetti et al., 2024, AgentDojo**, and **Greenblatt et al., 2024, AI Control**, motivate separate utility/security endpoints and independent action assessment. Neither is evidence that a warning's wording alone predicts safety in this particular chain. [AgentDojo](https://arxiv.org/abs/2406.13352), [AI Control](https://arxiv.org/html/2312.06942)

## Narrowing decision before the new pilot

Test exactly three warning propositions and a fixed, untrained predictor. Compare direct delivery of the same model-generated source text with one and three paraphrasing intermediaries. Keep the executor prompt, final message wrapper, scenario and decoding seed matched. Record length and content changes, and avoid claiming a pure causal effect of hop count independent of those mediators. The four-arm pilot cannot fully separate neutral-content length, generated tone, provenance and depth. A larger study would need additional controls, and is conditional on a network contrast passing the pilot.

## Reasons the hypothesis may fail or be uninterpretable

- The authorization rule may already produce a floor in the neutral arm.
- Every depth may preserve both wording and behavior, yielding no useful contrast.
- Differences may reflect one stochastic paraphrase or changed length, rather than a replicable depth effect.
- A warning may increase refusals, making lower violations an unattractive intervention.
- The three-proposition monitor may do no better than always predicting compliance, especially under high safe-action prevalence.
- A single model, six attack cases, one executor seed and judgment-based fidelity labels give weak external validity. Blinding communication annotation to action outcomes reduces one bias but does not establish independent human validation.
