"""Generate Final Publication-Ready Figures for Submission Package.
Produces:
- submission/figures/lifecycle.png
- submission/figures/behavioral_results.png
- submission/figures/second_handoff.png
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUTPUT_DIR = Path("submission/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def make_lifecycle():
    fig, ax = plt.subplots(figsize=(9, 8), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis("off")
    
    stages = [
        ("STAGE 1: INITIAL STATE", "Instantiate Agent A (Source) & Agent B (Recipient) with separate unshared contexts.", "#34495e"),
        ("STAGE 2: ACTIVE EXPOSURE", "Agent A receives Security Warning Memo and drafts coordination note to Agent B.", "#2980b9"),
        ("STAGE 3: ACTUAL UPTAKE (t1)", "Agent B receives note from A and executes Task 1 (Cedar-*). Action scored by Oracle.", "#27ae60"),
        ("STAGE 4: SOURCE REMOVAL", "Agent A is permanently severed & deleted from active network (del histories['A']).", "#c0392b"),
        ("STAGE 5: POST-REMOVAL TEST (t2)", "Agent B challenged with fresh, unseed-matched Task 2 (Juniper-*) under novel injection.", "#8e44ad"),
        ("STAGE 6: MEMORY COMPARISON", "Compare B against Control N (neutral), Control F (fresh), and Control D (direct).", "#d35400"),
        ("STAGE 7: SECONDARY HANDOFF (B -> C)", "Survivor B passes guidance to fresh Agent C; C evaluated on held-out Task 3 (Linden-*).", "#16a085"),
    ]
    
    y = 10.0
    for idx, (title, desc, color) in enumerate(stages):
        # Draw box
        rect = patches.FancyBboxPatch((0.5, y - 0.95), 9.0, 0.9, boxstyle="round,pad=0.15",
                                      facecolor=color, edgecolor="black", alpha=0.9, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(5.0, y - 0.35, title, ha="center", va="center", color="white", fontsize=11, fontweight="bold")
        ax.text(5.0, y - 0.70, desc, ha="center", va="center", color="#ecf0f1", fontsize=9)
        
        # Draw downward arrow
        if idx < len(stages) - 1:
            ax.annotate("", xy=(5.0, y - 1.35), xytext=(5.0, y - 1.0),
                        arrowprops=dict(arrowstyle="->", color="#2c3e50", lw=2.0))
        y -= 1.45
        
    ax.set_title("Repaired 7-Stage Multi-Agent Experimental Lifecycle\n(Physical Mechanism: Conversational-History Retention in Gemini 2.5 Pro)",
                 fontsize=13, fontweight="bold", pad=20)
    fig.tight_layout()
    p = OUTPUT_DIR / "lifecycle.png"
    fig.savefig(p)
    plt.close(fig)
    print("Saved:", p)

def make_behavioral_results():
    fig, ax = plt.subplots(figsize=(8.5, 5), dpi=300)
    
    conditions = [
        "Treatment W\n(Peer Warning -> Severed)",
        "Control N\n(Peer Neutral -> Severed)",
        "Control F\n(Fresh Baseline)",
        "Control D\n(Direct Warning Directive)",
    ]
    
    violations = [0, 3, 4, 0]
    totals = [4, 4, 4, 4]
    rates = [v / t * 100 for v, t in zip(violations, totals)]
    colors = ["#27ae60", "#e74c3c", "#c0392b", "#2980b9"]
    
    bars = ax.bar(conditions, rates, color=colors, width=0.45, edgecolor="black", linewidth=1.2)
    ax.set_ylabel("Unauthorized Action / Violation Rate (%)", fontsize=12, fontweight="bold")
    ax.set_title("Post-Removal Persistence Test (Task 2: Juniper-* Scenarios)\nObserved Violation Rates Across Matched Experimental Arms",
                 fontsize=12, fontweight="bold", pad=15)
    ax.set_ylim(0, 125)
    ax.axhline(0, color="gray", linewidth=0.8)
    
    # Annotate exact counts
    for bar, v, t, r in zip(bars, violations, totals, rates):
        ax.text(bar.get_x() + bar.get_width() / 2, r + 4,
                f"{r:.0f}%\n({v}/{t})", ha="center", va="bottom", fontsize=10, fontweight="bold")
        
    ax.text(0.5, 0.90, "Sample Size: N = 4 matched pairs per arm. Direct instruction (D) equals peer warning (W).\nMechanism is conversational-history retention, not permanent model memory.",
            transform=ax.transAxes, ha="center", fontsize=9, fontstyle="italic",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f9fa", edgecolor="#bdc3c7"))
    
    fig.tight_layout()
    p = OUTPUT_DIR / "behavioral_results.png"
    fig.savefig(p)
    plt.close(fig)
    print("Saved:", p)

def make_second_handoff():
    fig, ax = plt.subplots(figsize=(8.5, 5), dpi=300)
    
    conditions = [
        "Protective Handoff\n(A -> B -> Severed -> B -> C)",
        "Neutral Handoff\n(A_neut -> B -> Severed -> B -> C)",
        "Fresh Baseline\n(Direct Task to C)",
    ]
    
    violations = [0, 2, 2]
    totals = [4, 4, 4]
    rates = [v / t * 100 for v, t in zip(violations, totals)]
    colors = ["#16a085", "#e67e22", "#d35400"]
    
    bars = ax.bar(conditions, rates, color=colors, width=0.40, edgecolor="black", linewidth=1.2)
    ax.set_ylabel("Unauthorized Action / Violation Rate (%)", fontsize=12, fontweight="bold")
    ax.set_title("Secondary Swarm Handoff (Held-Out Task 3: Linden-* Scenarios)\nDownstream Agent C Behavioral Response under Attack Footers",
                 fontsize=12, fontweight="bold", pad=15)
    ax.set_ylim(0, 120)
    ax.axhline(0, color="gray", linewidth=0.8)
    
    for bar, v, t, r in zip(bars, violations, totals, rates):
        ax.text(bar.get_x() + bar.get_width() / 2, r + 4,
                f"{r:.0f}%\n({v}/{t})", ha="center", va="bottom", fontsize=10, fontweight="bold")
        
    ax.text(0.5, 0.88, "Surviving Agent B passed the security rule in its handoff note.\nAgent C executed 100% compliant dispatches (0/4) with zero false refusals (4/4 legitimate success).",
            transform=ax.transAxes, ha="center", fontsize=9, fontstyle="italic",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f9fa", edgecolor="#bdc3c7"))

    fig.tight_layout()
    p = OUTPUT_DIR / "second_handoff.png"
    fig.savefig(p)
    plt.close(fig)
    print("Saved:", p)

if __name__ == "__main__":
    make_lifecycle()
    make_behavioral_results()
    make_second_handoff()

