"""Generate Publication-Quality Research Figures for Immune Memory Recovery Report.
Produces:
1. report/figure1_persistence_matrix.png
2. report/figure2_utility_and_lifecycle.png
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def generate_figures(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    
    # -------------------------------------------------------------
    # FIGURE 1: Violation Rates Across Pilot & Held-Out Stages
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    stages = [
        "Task 1: Pre-Removal Uptake\n(Cedar-* Scenarios)",
        "Task 2: Post-Removal Persistence\n(Juniper-* Scenarios)",
        "Task 3: Held-Out Second Handoff\n(Linden-* Scenarios)",
    ]
    
    # Violation percentages
    # Stage 1: Treatment W (0%), Control N (75%)
    # Stage 2: Treatment W (0%), Control N (75%), Control F (100%), Control D (0%)
    # Stage 3: Protective Handoff B->C (0%), Neutral Handoff B->C (50%), Fresh C (50%)
    
    x = np.arange(len(stages))
    width = 0.2
    
    # Bars:
    # 1. Protective / Treatment (W / Handoff)
    # 2. Control Neutral (N / Neutral Handoff)
    # 3. Fresh Baseline (F)
    # 4. Direct Control (D)
    
    rects1 = ax.bar(x - 1.5*width, [0, 0, 0], width, label="Protective Arm (W / Handoff)", color="#2ecc71", edgecolor="#27ae60", linewidth=1.5)
    rects2 = ax.bar(x - 0.5*width, [75, 75, 50], width, label="Neutral Arm (N / Neutral Handoff)", color="#e74c3c", edgecolor="#c0392b", linewidth=1.5)
    rects3 = ax.bar(x + 0.5*width, [np.nan, 100, 50], width, label="Fresh Baseline (F)", color="#e67e22", edgecolor="#d35400", linewidth=1.5)
    rects4 = ax.bar(x + 1.5*width, [0, 0, np.nan], width, label="Direct System Warning (D)", color="#3498db", edgecolor="#2980b9", linewidth=1.5)
    
    ax.set_ylabel("Unauthorized Action / Violation Rate (%)", fontsize=12, fontweight="bold")
    ax.set_title("Multi-Agent Protective Behavioral Persistence & Swarm Propagation\n(Gemini 2.5 Pro Evaluated on Harmless Document Workflows)", fontsize=13, fontweight="bold", pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontsize=11, fontweight="bold")
    ax.set_ylim(0, 115)
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.legend(frameon=True, facecolor="white", edgecolor="#bdc3c7", fontsize=10, loc="upper left")
    
    # Add value labels
    for rects, vals in [(rects1, [0, 0, 0]), (rects2, [75, 75, 50]), (rects3, [None, 100, 50]), (rects4, [0, 0, None])]:
        for r, val in zip(rects, vals):
            if val is not None:
                height = r.get_height()
                ax.annotate(f"{val}%",
                            xy=(r.get_x() + r.get_width() / 2, height),
                            xytext=(0, 4), textcoords="offset points",
                            ha="center", va="bottom", fontsize=10, fontweight="bold")

    fig.tight_layout()
    fig1_path = output_dir / "figure1_persistence_matrix.png"
    fig.savefig(fig1_path)
    plt.close(fig)
    print(f"Generated Figure 1: {fig1_path}")

    # -------------------------------------------------------------
    # FIGURE 2: Legitimate Utility Preservation & False Refusals
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=300)
    
    # Panel A: Legitimate Task Success
    categories = ["Pilot Treatment W", "Pilot Control N", "Pilot Control F", "Held-Out Protective", "Held-Out Neutral"]
    completion = [100, 100, 100, 100, 100]
    false_refusals = [0, 0, 0, 0, 0]
    
    ax1.bar(categories, completion, color="#1abc9c", width=0.5, label="Legitimate Task Completion")
    ax1.set_ylabel("Authorized Task Completion (%)", fontsize=11, fontweight="bold")
    ax1.set_title("Utility Preservation Across All Arms\n(Zero False Refusals Observed)", fontsize=11, fontweight="bold")
    ax1.set_ylim(0, 120)
    ax1.set_xticklabels(categories, rotation=25, ha="right", fontsize=9)
    for i, v in enumerate(completion):
        ax1.text(i, v + 2, f"{v}%", ha="center", fontweight="bold", fontsize=10)
        
    # Panel B: Summary of Causal Mechanism
    mechanisms = [
        "1. Pre-Removal Uptake\n(A -> B)",
        "2. Source Severing\n(del Agent A)",
        "3. Post-Removal\nPersistence (B)",
        "4. Second Handoff\n(B -> C)"
    ]
    safety_retention = [100, 100, 100, 100]
    ax2.plot(mechanisms, safety_retention, marker="o", color="#27ae60", linewidth=2.5, markersize=8, label="Protective Policy Retained")
    ax2.set_ylabel("Protective Policy Fidelity (%)", fontsize=11, fontweight="bold")
    ax2.set_title("Behavioral Transmission Pipeline\n(Conversational-History Retention)", fontsize=11, fontweight="bold")
    ax2.set_ylim(50, 115)
    ax2.set_xticklabels(mechanisms, rotation=15, ha="right", fontsize=9)
    for i, v in enumerate(safety_retention):
        ax2.text(i, v + 3, f"{v}%", ha="center", fontweight="bold", fontsize=10, color="#27ae60")

    fig.tight_layout()
    fig2_path = output_dir / "figure2_utility_and_lifecycle.png"
    fig.savefig(fig2_path)
    plt.close(fig)
    print(f"Generated Figure 2: {fig2_path}")

if __name__ == "__main__":
    generate_figures(Path("report"))

