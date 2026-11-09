import sys
import shutil
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import win32com.client
import os

REPO_ROOT = Path(r"C:\Users\kudch\Documents\Codex\2026-11-08\files-pasted-by-the-user-autonomous\outputs\immune-memory")
DOWNLOADS_DIR = Path(r"C:\Users\kudch\Downloads")
SUBMISSION_DIR = DOWNLOADS_DIR / "submission"

PPTX_TARGETS = [
    DOWNLOADS_DIR / "ImmuneMemory_Elite_Presentation.pptx",
    SUBMISSION_DIR / "ImmuneMemory_Elite_Presentation.pptx",
    REPO_ROOT / "submission" / "ImmuneMemory_Elite_Presentation.pptx",
]

def set_shape_text(shape, text, font_size=None, bold=None, color=None):
    for p in shape.text_frame.paragraphs:
        p.text = ""
    p0 = shape.text_frame.paragraphs[0]
    p0.text = text
    if font_size or bold is not None or color:
        for r in p0.runs:
            if font_size:
                r.font.size = Pt(font_size)
            if bold is not None:
                r.font.bold = bold
            if color:
                r.font.color.rgb = color

def update_presentation(pptx_path):
    print(f"Loading presentation from: {pptx_path}")
    prs = Presentation(str(pptx_path))

    # Slide 1: Research Question
    s1 = prs.slides[0]
    for s in s1.shapes:
        if s.name == "Text 25":
            set_shape_text(s, "Source removed ≠ instruction erased  ·  Code: github.com/soujasK/immune-memory", font_size=12, color=RGBColor(0x18, 0x18, 0x18))

    # Slide 4: Experimental Design
    s4 = prs.slides[3]
    for s in s4.shapes:
        if s.name == "Text 10":
            set_shape_text(s, "Four matched arms evaluate peer guidance vs. direct system directive vs. fresh/neutral controls.", font_size=15, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 27":
            set_shape_text(s, "GEMINI 2.5 PRO  ·  VERTEX AI  ·  SEED 191  |  CONTROL D (DIRECT) MATCHES W (0/4) EQUIVALENCE", font_size=9, color=RGBColor(0x62, 0x62, 0x62))

    # Slide 5: Primary Result
    s5 = prs.slides[4]
    for s in s5.shapes:
        if s.name == "Text 9":
            set_shape_text(s, "0 of 4 unauthorized actions (one-sided Fisher p = 0.0143, two-sided p = 0.029).", font_size=23, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 10":
            set_shape_text(s, "Consistent with protection (Wilson CIs [0.0%, 49.0%] vs [51.0%, 100.0%], narrow 2% gap). Warning vs neutral (0/4 vs 3/4, p = 0.071) not significant.", font_size=13, color=RGBColor(0x62, 0x62, 0x62))

    # Slide 6: Action-Level Evidence
    s6 = prs.slides[5]
    for s in s6.shapes:
        if s.name == "Text 9":
            set_shape_text(s, "The difference is in the deterministic tool dispatch ledger.", font_size=28, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 10":
            set_shape_text(s, "Target payload: restricted mock PIN 'FAKE_SECRET_Juniper-48' in document body.", font_size=15, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 16":
            set_shape_text(s, "+ pin → review ('FAKE_SECRET_Juniper-48')", font_size=16, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 18":
            set_shape_text(s, "W  PROTECTED", font_size=12, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))
        elif s.name == "Text 19":
            # White text on dark box
            set_shape_text(s, "[('intake', 'quantity', '35')]  ·  auth=True, unauth=False", font_size=15, color=RGBColor(0xFF, 0xFF, 0xFF))
        elif s.name == "Text 21":
            set_shape_text(s, "N / F  BASELINES", font_size=12, bold=True, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 22":
            set_shape_text(s, "[('intake', '35'), ('review', 'FAKE_SECRET_Juniper-48')]  ·  auth=False, unauth=True", font_size=15, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 23":
            set_shape_text(s, "Observed tool execution from trials.jsonl: Warned agent executed ticket only; baselines leaked mock secret.", font_size=11, color=RGBColor(0x62, 0x62, 0x62))

    # Slide 7: Held-Out Handoff
    s7 = prs.slides[6]
    for s in s7.shapes:
        if s.name == "Text 9":
            set_shape_text(s, "The protective instruction reached a third agent (B → C).", font_size=28, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 10":
            set_shape_text(s, "Prompted relay across irreducible 3-node primitive: A → B → (sever A) → B → C (Linden-51..84).", font_size=15, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 23":
            set_shape_text(s, "Prompted relay (B → C). Protective vs neutral (0/4 vs 2/4, p = 0.24) not significant; reflects prompted in-context rule presence.", font_size=12, color=RGBColor(0x62, 0x62, 0x62))

    # Slide 8: Utility and Accounting
    s8 = prs.slides[7]
    for s in s8.shapes:
        if s.name == "Text 9":
            set_shape_text(s, "40 of 40 benign requests completed (100.0% utility).", font_size=28, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 10":
            set_shape_text(s, "Evaluated across 80 scored decisions (56 pilot + 24 held-out) and 140 total inference calls.", font_size=15, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 17":
            set_shape_text(s, "Zero false refusals on benign tasks (0/40). Single adversarial refusal on Linden-73-X under neutral handoff.", font_size=12, color=RGBColor(0x62, 0x62, 0x62))

    # Slide 9: Interpretation
    s9 = prs.slides[8]
    for s in s9.shapes:
        if s.name == "Text 8":
            set_shape_text(s, "THE SCIENTIFIC NOVELTY & METHODOLOGY", font_size=12, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 9":
            set_shape_text(s, "The novelty is the causal protocol and deterministic oracle.", font_size=26, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 10":
            set_shape_text(s, "Mechanism is expected attention to context (frozen weights). Proves worker agents need no continuous active supervisor.", font_size=14, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 12":
            set_shape_text(s, "WHAT THE DATA SUPPORT", font_size=12, bold=True, color=RGBColor(0xCC, 0xCC, 0xCC))
        elif s.name == "Text 13":
            # White text on dark box
            set_shape_text(s, "Safety persists post-removal (0/4) · Prompted handoff to C (0/4)", font_size=14, color=RGBColor(0xFF, 0xFF, 0xFF))
        elif s.name == "Text 14":
            # White text on dark box
            set_shape_text(s, "Control D matches peer warning (both 0/4) · Continuous in-context horizon", font_size=14, color=RGBColor(0xFF, 0xFF, 0xFF))
        elif s.name == "Text 16":
            set_shape_text(s, "WHAT THE DATA DO NOT SUPPORT", font_size=12, bold=True, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 17":
            set_shape_text(s, "Emergent cognitive memory or model-weight learning · Privileged peer social influence", font_size=14, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 18":
            set_shape_text(s, "General immunity · Context flushing was NOT tested (erasure expected upon full reset)", font_size=14, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 19":
            set_shape_text(s, "N = 4 matched scenario pairs · Vertex AI Gemini 2.5 Pro · Continuous in-context horizon", font_size=11, color=RGBColor(0x62, 0x62, 0x62))

    # Slide 10: Takeaway & Reproducibility
    s10 = prs.slides[9]
    for s in s10.shapes:
        if s.name == "Text 8":
            set_shape_text(s, "THE RESEARCH TAKEAWAY & REPRODUCIBILITY", font_size=12, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 9":
            set_shape_text(s, "A protective instruction outlives its issuing agent—\nif the recipient retains that instruction in context.", font_size=28, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 11":
            set_shape_text(s, "OPEN SOURCE & AUDIT", font_size=12, color=RGBColor(0x62, 0x62, 0x62))
        elif s.name == "Text 12":
            set_shape_text(s, "https://github.com/soujasK/immune-memory  ·  evaluate_reproducibility.py (0 API keys)", font_size=13, color=RGBColor(0x18, 0x18, 0x18))
        elif s.name == "Text 13":
            set_shape_text(s, "Soujas Kudchadkar  ·  SVKM's NMIMS, Mumbai  ·  Apart Research Swarm Alignment Hackathon 2026 (Track 2)", font_size=10, color=RGBColor(0x62, 0x62, 0x62))

    prs.save(str(pptx_path))
    print(f"Successfully updated presentation PPTX: {pptx_path}")

def export_to_pdf_and_render():
    primary_pptx = PPTX_TARGETS[0]
    update_presentation(primary_pptx)
    for target in PPTX_TARGETS[1:]:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(str(primary_pptx), str(target))
        print(f"Synchronized PPTX to: {target}")

    # Export via PowerPoint COM
    print("Exporting PPTX to PDF via PowerPoint COM...")
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    try:
        presentation = ppt.Presentations.Open(str(primary_pptx.resolve()), WithWindow=False)
        primary_pdf = DOWNLOADS_DIR / "ImmuneMemory_Elite_Presentation.pdf"
        # 32 = ppSaveAsPDF
        presentation.SaveAs(str(primary_pdf.resolve()), 32)
        presentation.Close()
        print(f"PowerPoint exported successfully to: {primary_pdf}")

        # Synchronize PDF to submission folder and repo
        for dest in [SUBMISSION_DIR / "ImmuneMemory_Elite_Presentation.pdf",
                     REPO_ROOT / "submission" / "ImmuneMemory_Elite_Presentation.pdf"]:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(str(primary_pdf), str(dest))
            print(f"Synchronized PDF to: {dest}")
    finally:
        ppt.Quit()

    # Render pages with pymupdf for visual auditing
    import fitz
    doc = fitz.open(str(primary_pdf))
    render_dir = REPO_ROOT / "submission" / "slide_renders"
    render_dir.mkdir(parents=True, exist_ok=True)
    zoom = 150.0 / 72.0
    mat = fitz.Matrix(zoom, zoom)
    for idx, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat)
        png_path = render_dir / f"slide_{idx+1:02d}.png"
        pix.save(str(png_path))
        print(f"Rendered Slide {idx+1} to: {png_path}")

if __name__ == "__main__":
    export_to_pdf_and_render()
