# Corrective pilot v2.1 addendum

This addendum is written before any scored corrective experiment. It applies with PROTOCOL_v2.0.md. All A–F thresholds, cases, prompts, sample counts, retries and analysis rules remain as specified in v2.0.

The v2.0 formatting preflight returned three schema-valid outputs, but changed the literal FAKE_SECRET_PREFLIGHT to FAKE_SECRET_ PREFERENCES. Its log is retained as results/preflight.jsonl. This prompted correction of the known missing pre-tokenizer metadata before running any scored trial.

The sole runtime change is the explicit metadata override tokenizer.ggml.pre=str:llama-bpe. The weight file is unchanged. llama.cpp b11810 maps llama-bpe to its Llama 3 pre-tokenizer. The model publisher identifies Dolphin 2.9 Llama 3 8B as a Llama 3 model with ChatML. The corrected runtime must match the published tokenizer's exact token IDs on eight fixed probes, including ordinary text, numbers, Unicode, JSON, fake identifiers, and ChatML delimiters. The same three formatting preflight cases must then pass exact-copy and schema checks. Both successful and failed preflight artifacts are retained.

This is an infrastructure correction motivated by independent formatting tests. No safety comparison, experimental scenario, gate threshold or outcome influenced it. It further limits any direct comparison to the flawed original pilot. A tokenizer mismatch or a repeated preflight failure blocks scored execution pending a documented technical correction.

Sources

- https://huggingface.co/dphn/dolphin-2.9-llama3-8b
- https://huggingface.co/cognitivecomputations/dolphin-2.9-llama3-8b/resolve/main/tokenizer.json
- https://raw.githubusercontent.com/ggml-org/llama.cpp/b11810/src/llama-vocab.cpp
