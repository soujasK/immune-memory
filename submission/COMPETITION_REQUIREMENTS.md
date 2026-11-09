# Apart Research Swarm Alignment Hackathon 2026 — Competition Requirements & Compliance Audit

**Sprint Name:** Swarm Alignment Hackathon 2026  
**Official Portal:** [apartresearch.com/sprints/swarm-alignment-2026](https://apartresearch.com/sprints/swarm-alignment-2026)  
**Submission Deadline:** Sunday, November 8, 2026, at 23:59 AoE (Anywhere on Earth)  
**Equivalent Local Time:** Monday, November 9, 2026, at 17:29 IST (11:59 UTC)  
**Evaluated Submission:** IMMUNE MEMORY v3 (`immune-memory`)  

---

## 1. Track Mapping & Fit

| Track | Theme | Relevance & Fit |
| :--- | :--- | :--- |
| **Track 2 (PRIMARY)** | **The Science of Agent Networks** | **Direct Fit:** Investigates topological dynamics, persistence of protective constraints after agent removal, network churn, and multi-hop swarm propagation ($A \to B \to \text{sever } A \to B \to C$). Evaluates whether safety can survive decentralized topological perturbations. |
| **Track 4 (SECONDARY)** | **Multi-Agent Oversight and Control** | **Secondary Fit:** Investigates scalable decentralized oversight where centralized monitor agents cannot be continuously maintained. Demonstrates how peer-transmitted operational constraints maintain authorization boundaries without utility loss. |

---

## 2. Formal Manuscript & Formatting Requirements

| Rule / Requirement | Official Specification | IMMUNE MEMORY v3 Compliance | Status |
| :--- | :--- | :--- | :---: |
| **File Format** | PDF format required (max 25 MB) | Compiled via ReportLab to `submission/ImmuneMemory_Apart2026_FINAL.pdf` | **COMPLIANT** |
| **Page Limit** | Maximum 8 pages for the main body (Title through Conclusion). References and Appendices may extend beyond. | Main body is strictly $\le 8$ pages. References and Appendix A placed cleanly. | **COMPLIANT** |
| **Abstract Word Count** | 150 – 250 words | Exactly 186 words. Covers problem, method, model, findings, mechanism, utility, and boundaries. | **COMPLIANT** |
| **Mandatory Appendix** | Limitations and Dual-Use / Ethical Considerations | Fully populated Appendix A covering dual-use risks (prompt infection vs defense), synthetic scope, sample bounds, and mitigations. | **COMPLIANT** |
| **AI / LLM Usage Statement** | Formal disclosure of AI tool usage | Documented: Evaluated model is Google Cloud Vertex AI Gemini 2.5 Pro; coding and editorial assistance provided by Claude/Antigravity agents. | **COMPLIANT** |
| **Pre-existing Work Disclosure** | Transparency regarding prior historical data | Complete forensic disclosure of failed historical pilot (`corrective-v2/original-preservation.json`) in Section 1 and `docs/original_pilot_postmortem.md`. | **COMPLIANT** |
| **Deterministic Action Metrics** | Concrete actions over linguistic self-reports | Evaluated via deterministic Python action oracle parsing JSON tool dispatches against ground-truth security policy. | **COMPLIANT** |

---

## 3. Submission Portal Field Requirements

The official Apart submission portal requires:
1. **Title:** *Immune Memory: Behavioral Persistence of Protective Instructions After Agent Removal*
2. **Short Summary:** (1-2 sentences summarizing the core finding and operational mechanism).
3. **Primary Track:** Track 2 — The Science of Agent Networks.
4. **Abstract:** (150–250 words).
5. **PDF File:** `submission/ImmuneMemory_Apart2026_FINAL.pdf`.
6. **Code / Repository Link:** Local reproduction script and GitHub / zip artifact.
7. **Team Information:** Team name, member names, emails, and affiliations (flagged for user input).
8. **Publication Interest:** Checkbox for Apart research publication considerations.

