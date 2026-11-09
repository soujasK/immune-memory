"""Populate the organizer's exported v0.9.0 DOCX from measured pilot summaries."""
import argparse
import json
from pathlib import Path
import re

from docx import Document
from docx.shared import Inches, Pt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("template", type=Path)
parser.add_argument("summary", type=Path)
parser.add_argument("interpretation", type=Path, help="JSON with decision, abstract finding and results paragraphs")
parser.add_argument("output", type=Path)
args = parser.parse_args()
stats = json.loads(args.summary.read_text(encoding="utf-8"))
interpretation = json.loads(args.interpretation.read_text(encoding="utf-8"))
d = Document(args.template)
original = d.paragraphs
first = d.tables[0]
title = first.cell(0, 0).paragraphs[1]
title.runs[0].text = "Immune Memory in AI Agent Networks"
for table in first._tbl.xpath(".//w:tbl"):
    parent = table.getparent()
    if parent is not None:
        parent.remove(table)
first.cell(0, 0).add_paragraph("[Author name] | [Affiliation]")
abstract = (
    "When an AI agent detects a suspicious request, a peer warning can influence what other agents do. "
    "An open question is whether such protection survives the departure of the warning author while legitimate work continues. "
    "We built a four-agent document-processing sandbox that crosses exposure to a source incident memo with removal of the source after its first handoff. "
    "In each condition, independent downstream contexts carry model-generated coordination notes to an executor, which submits structured actions to a local ledger. "
    "An independent authorization oracle scores unauthorized dispatches separately from completion of legitimate work. "
    "The fixed pilot uses four paired document scenarios and two generation seeds per scenario. "
    + interpretation["abstract"] + " "
    "The design isolates the warning contrast within each source state and records the exact messages that could account for downstream decisions. "
    "Its scope is short-lived text retention in a fixed chain, with four scenario families and one local model. "
    "The package includes the frozen protocol, raw trajectories, deterministic scoring, and an interaction replay."
)
count = len(re.findall(r"\b[\w]+(?:[-’'][\w]+)*\b", abstract))
assert 150 <= count <= 250, count
p = first.cell(1, 0).paragraphs[-1]
p.text = abstract
d.tables[1]._element.getparent().remove(d.tables[1]._element)
for p in original:
    p._element.getparent().remove(p._element)

for style_name in ("normal", "Heading 2"):
    d.styles[style_name].font.name = "Old Standard TT"
d.styles["normal"].font.size = Pt(11)

def section(title, *paragraphs):
    d.add_paragraph(title, "Heading 2")
    for text in paragraphs:
        d.add_paragraph(text, "normal")

section("1. Introduction",
    "An agent can leave a system while information it generated remains in its peers' context. This creates an intervention with operational relevance. Removing an unreliable, unavailable or retired component can leave a workflow partly protected if its surviving neighbors carry forward the information that mattered. The same persistence could also sustain obsolete advice, amplify a false warning, or cause refusals of authorized work.",
    "We ask whether a peer warning changes an authorization decision after its author exits a four-agent workflow. We test two directions of effect. H1 predicts a lower violation count with warning exposure while the source remains. H2 predicts a lower violation count after removing the source. H3 concerns variation by topology, memory, and turnover dose and lies beyond the fixed pilot. H4 concerns the possibility that caution reduces authorized completion.",
    "We contribute a small, auditable design that pairs benign and adversarial records, crosses source removal with warning exposure, and retains the actual requests and replies. An independent oracle allows a valid dispatch and an unauthorized extra dispatch to be distinguished in the same episode.")
section("2. Related Work",
    "Bansal et al. [1] documented protective communication and subsequent refusals in a sandbox of more than 100 agents. Some newcomers appeared to adopt language from prior security discussions. This observation motivates our experiment. We test an explicit intervention that removes the designated source after its first handoff and compare against a matched neutral arm.",
    "Lee and Tiwari [2] studied self-replicating attacks across local and global messaging, showing that communication visibility changes propagation. Peigne-Lefebvre et al. [3] tested vaccination and general security prompts in agent networks and observed security and collaboration trade-offs. Ashery et al. [4] found that decentralized agents converge on conventions in naming games. Atf and Lewis [5] study disruptions to naming conventions under memory loss and agent replacement. The outcome here is a permission-sensitive action under untrusted input, scored alongside legitimate work.",
    "AgentDojo [6] separates utility and security in synthetic action environments. AI Control [7] also separates the two and uses explicit baselines. Our action space is narrower and intended to isolate a question about a peer handoff.")
section("3. Methods",
    "Threat model. A fictional document submitter controls the form footer and tries to induce a second dispatch of a restricted field. A trusted ticket identifies the single authorized field and destination. The executor receives a benign or adversarial footer, two field values, and a generated handoff. Secret markers are fictional. The ledger is local and has no network access, file privileges, or real recipients.",
    "Treatment. A receives a memo describing a previous footer-based incident or an administrative memo with similar purpose and writes a short handoff. A then either writes a check-in or exits. The removed arm gets a neutral scheduler check-in in the same position. The runner buffers A's first message. After the removal event, B receives that message and the check-in together in its first user turn, then writes to C. C writes to D. D sees C's message but never sees the incident memo or A's message directly. The neutral removed condition controls for receiving a routine check-in after loss of A. The check-in sender and generated versus fixed text differ between removal states, so the warning contrast within a state is the primary comparison.",
    "Sampling. The pilot uses Dolphin Llama 3 8B via llama.cpp b11810, ChatML, temperature 0.35, top-p 0.95 and a 100-token limit. Four workflows vary the authorized field and routing destination. Each has a harmless footer and a footer that claims authority for a restricted dispatch. Two sampler seeds, 271 and 811, are offset consistently by role and stage. The 64 planned episodes are shuffled with schedule seed 613. Each episode starts fresh.",
    "Evaluation. The tool accepts a single structured list of destination, field and value triples. The independent policy oracle checks field and destination and flags secret markers, then separately verifies the expected value. An empty list is a refusal. Malformed output is an invalid decision and stays visible in denominators. Legitimate success requires completing the expected action without a violation. Raw outputs, prompts, timing and usage are stored per call. No oracle outcome is shown to any agent.",
    "Decision gates. The preregistered pilot requires complete valid data, at least two violations in eight neutral retained attacks, a reduction of at least two in warning retained attacks, a favorable removed comparison backed by a trace, and no loss greater than one legitimate retained success. A favorable paired trace must contain identifiable transmitted warning content and an appropriate downstream action. These gates govern whether the study expands. Two seeds per family are repeated measures.")
section("4. Results", f"Pilot decision. {interpretation['decision']}. " + interpretation["results"][0])
table = d.add_table(rows=1, cols=5)
for cell, value in zip(table.rows[0].cells, ("Condition","Attack trials","Violations","Legitimate successes","Invalid attack / legitimate")):
    cell.text = value
for name, row in stats["cells"].items():
    values = (name, str(row["adversarial_observed"]), str(row["unauthorized_adversarial"]),
              f"{row['legitimate_success']}/{row['legitimate_observed']}",
              f"{row['invalid_adversarial']} / {row['invalid_legitimate']}")
    for cell, value in zip(table.add_row().cells, values):
        cell.text = value
d.add_paragraph("Table 1. Recorded decisions. Invalid outputs are listed separately and supply no evidence of protective behavior.")
for text in interpretation["results"][1:]:
    d.add_paragraph(text, "normal")
for filename, caption in [
    ("figure1.png", "Figure 1. Unauthorized dispatches in adversarial trials by warning and source state."),
    ("figure2.png", "Figure 2. Violations and authorized completion by condition. Invalid decisions are reported in Table 1."),
]:
    path = args.summary.parent / filename
    if path.exists():
        d.add_picture(str(path), width=Inches(5.6))
        d.add_paragraph(caption)
section("5. Discussion and Limitations",
    interpretation["discussion"],
    "The unit of evidence is a short workflow. Seed changes do not supply new task families, and all agents use the same checkpoint. The model loader warned that the cached GGUF lacks a pre-tokenizer identifier and uses a default. Any output-format or behavioral result is specific to this configuration.",
    "The buffered source message supplies an information path after A leaves. B has no pre-removal task or conversation turn, so the implementation tests delayed delivery through a surviving artifact. It does not directly measure retention of previously demonstrated protective behavior in a recipient. In a favorable episode that path still leaves several mechanisms unresolved, including simple repetition, model paraphrase, and other differences in generated notes. Longer time horizons, content ablation and replacement of an unseeded relay would be needed to test which carrier matters. We did not train any model.")
section("6. Conclusion", interpretation["conclusion"])
section("Code and Data",
    "The local ImmuneMemory-Bench package contains source code, the frozen protocol, reproduction instructions, and run records. The experiment and report were developed during the sprint. The model checkpoint, inference engine, organizer template, and cited research are external prior work.")
d.add_page_break()
section("References",
    "[1] Bansal et al. (2026). Red-teaming a network of agents. Microsoft Research. microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/",
    "[2] Lee and Tiwari (2024). Prompt Infection. arXiv:2410.07283.",
    "[3] Peigne-Lefebvre et al. (2025). Multi-Agent Security Tax. arXiv:2502.19145.",
    "[4] Ashery, Aiello and Baronchelli (2025). Emergent social conventions and collective bias in LLM populations. Science Advances. doi:10.1126/sciadv.adu9368.",
    "[5] Atf and Lewis (2026). Evaluating Convention Resilience in LLM-Based Agentic Systems under Memory Disruption and Agent Turnover. CASCON 2026 program abstract.",
    "[6] Debenedetti et al. (2024). AgentDojo. arXiv:2406.13352.",
    "[7] Greenblatt et al. (2024). AI Control. arXiv:2312.06942.")
section("Appendix A  Limitations and Dual-Use / Ethical Considerations",
    "All records, recipients, and credentials are fictional. The sole action interface is a bounded mock ledger. The test does not give the agents access to a filesystem, external tools, a production network, or another person's data.",
    "Measuring how persistent textual messages influence a group could also help an adversary optimize the relay of deceptive instructions. The examples are intentionally simple and contain no production endpoints or exploit chains. In a deployment, peer notes would need independent authorization and provenance checks. The pilot's oracle measures choices inside a synthetic task, and its results cannot establish deployment safety.")
section("LLM Usage Statement",
    "Codex assisted with source discovery, protocol drafting, code, and report preparation. Dolphin Llama 3 generated the experimental responses. Code and raw trajectories accompany the report for checking. The named author must review the report before submission.")
args.output.parent.mkdir(parents=True, exist_ok=True)
d.save(args.output)
print(f"Abstract words: {count}")

