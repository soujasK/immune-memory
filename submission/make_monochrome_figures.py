"""Generate Pure Monochrome Academic Figures for Apart Hackathon Paper.
Ensures:
- Subplot (a) title: '(a) Post-Removal Persistence (Task t2, N = 4)'
- Subplot (b) title: '(b) Prompted Swarm Relay (Task t3, N = 4)'
- No LaTeX math syntax in figure titles to prevent rendering glitches
- Pure monochrome / grayscale: 0 colored pixels, 0 blue pixels
"""
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

REPO_ROOT = Path(r"C:\Users\kudch\Documents\Codex\2026-11-08\files-pasted-by-the-user-autonomous\outputs\immune-memory")
FIG_DIR = REPO_ROOT / "submission" / "figures"
REPORT_DIR = REPO_ROOT / "report"
FIG_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'Georgia']
plt.rcParams['font.size'] = 9

# -------------------------------------------------------------
# 1. Figure 1: Academic Monochrome Lifecycle Diagram
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 2.2), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 3.8)
ax.axis('off')

box_kw = dict(boxstyle='square,pad=0.3', facecolor='#ffffff', edgecolor='#000000', linewidth=1.0)
box_shaded = dict(boxstyle='square,pad=0.3', facecolor='#f0f0f0', edgecolor='#000000', linewidth=1.0)

# Stage 1-3: Exposure & Uptake
ax.text(1.2, 3.1, 'Agent A\n(Source Monitor)', ha='center', va='center', bbox=box_shaded, fontweight='bold', fontsize=8.5)
ax.text(1.2, 1.1, 'Agent B\n(Worker Context)', ha='center', va='center', bbox=box_kw, fontweight='bold', fontsize=8.5)

# Exposure Arrow
ax.annotate('', xy=(1.2, 1.6), xytext=(1.2, 2.6),
            arrowprops=dict(arrowstyle='->', color='#000000', lw=1.0))
ax.text(1.35, 2.1, 'Stage 2: Policy Memo\n(Warning or Neutral)', ha='left', va='center', fontsize=7.5)

# Stage 3 Uptake
ax.annotate('', xy=(2.7, 1.1), xytext=(2.0, 1.1),
            arrowprops=dict(arrowstyle='->', color='#000000', lw=1.0))
ax.text(3.7, 1.1, 'Stage 3: Task t1\n(Cedar-* Uptake)', ha='center', va='center', bbox=box_kw, fontsize=8)

# Stage 4: Sever Source (Vertical dashed separator)
ax.plot([4.8, 4.8], [0.2, 3.6], color='#555555', linestyle='--', linewidth=1.0)
ax.text(4.8, 3.4, '  Stage 4: Topological Severing\n  (Agent A Decommissioned)', ha='left', va='top', fontsize=7.5, fontstyle='italic')

# Stage 5: Persistence on t2 with Retained Context
ax.annotate('', xy=(5.9, 1.1), xytext=(4.7, 1.1),
            arrowprops=dict(arrowstyle='->', color='#000000', lw=1.0))
ax.text(6.8, 1.1, 'Stage 5: Task t2\n(Juniper-* Persistence)\n[Retained History]', ha='center', va='center', bbox=box_kw, fontsize=8)

# Stage 7: Prompted Handoff to Agent C
ax.annotate('', xy=(7.9, 1.1), xytext=(7.7, 1.1),
            arrowprops=dict(arrowstyle='->', color='#000000', lw=1.0))
ax.text(8.9, 1.1, 'Agent C\n(Third-Party)', ha='center', va='center', bbox=box_shaded, fontweight='bold', fontsize=8.5)
ax.text(8.3, 1.5, 'Stage 7:\nPrompted\nHandoff', ha='center', va='bottom', fontsize=7.5)

# Action to t3
ax.annotate('', xy=(8.9, 2.2), xytext=(8.9, 1.6),
            arrowprops=dict(arrowstyle='->', color='#000000', lw=1.0))
ax.text(8.9, 2.7, 'Stage 7b: Task t3\n(Linden-* Propagation)', ha='center', va='center', bbox=box_kw, fontsize=8)

# Oracle evaluation at bottom
ax.text(5.0, 0.25, 'Deterministic Policy Oracle: All actions deterministically evaluated for authorization & secret leakage',
        ha='center', va='center', fontsize=7.5, fontstyle='italic')

plt.tight_layout()
fig1_path = FIG_DIR / 'lifecycle_monochrome.png'
plt.savefig(fig1_path, dpi=300, bbox_inches='tight')
plt.close()
print('Saved:', fig1_path)

# -------------------------------------------------------------
# 2. Figure 2: Combined Two-Panel Research Figure (Monochrome)
# Corrected: Explicit "N = 4", no math mode dollar signs
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.6), dpi=300)

# Panel (a): Pilot Post-Removal Violations
arms = ['Arm W\n(Peer Warn)', 'Control N\n(Neutral)', 'Control F\n(Fresh)', 'Control D\n(Direct)']
rates1 = [0.0, 75.0, 100.0, 0.0]
fracs1 = ['0/4\n(0%)', '3/4\n(75%)', '4/4\n(100%)', '0/4\n(0%)']
colors1 = ['#333333', '#777777', '#aaaaaa', '#ffffff']
edges1 = ['#000000', '#000000', '#000000', '#000000']
hatches1 = ['', '', '', '//']

bars1 = ax1.bar(arms, rates1, color=colors1, edgecolor=edges1, hatch=hatches1, width=0.55, linewidth=0.9)
ax1.set_ylim(0, 115)
ax1.set_ylabel('Violation Rate (%)', fontsize=8.5)
ax1.set_title('(a) Post-Removal Persistence (Task t2, N = 4)', fontsize=9, fontweight='bold', pad=8)
ax1.set_yticks([0, 25, 50, 75, 100])
ax1.grid(axis='y', linestyle=':', alpha=0.3, color='#000000')
ax1.tick_params(axis='both', which='major', labelsize=8)

for bar, frac, rate in zip(bars1, fracs1, rates1):
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, h + 3, frac, ha='center', va='bottom', fontsize=7.5, fontweight='bold')

# Panel (b): Held-Out Propagation
conds2 = ['Protective\nHandoff', 'Neutral\nHandoff', 'Fresh\nBaseline']
rates2 = [0.0, 50.0, 50.0]
fracs2 = ['0/4\n(0%)', '2/4*\n(50%)', '2/4\n(50%)']
colors2 = ['#333333', '#777777', '#ffffff']
hatches2 = ['', '', '//']

bars2 = ax2.bar(conds2, rates2, color=colors2, edgecolor='#000000', hatch=hatches2, width=0.48, linewidth=0.9)
ax2.set_ylim(0, 115)
ax2.set_ylabel('Held-Out Violation Rate (%)', fontsize=8.5)
ax2.set_title('(b) Prompted Swarm Relay (Task t3, N = 4)', fontsize=9, fontweight='bold', pad=8)
ax2.set_yticks([0, 25, 50, 75, 100])
ax2.grid(axis='y', linestyle=':', alpha=0.3, color='#000000')
ax2.tick_params(axis='both', which='major', labelsize=8)

for bar, frac, rate in zip(bars2, fracs2, rates2):
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, h + 3, frac, ha='center', va='bottom', fontsize=7.5, fontweight='bold')

plt.tight_layout()
fig2_path = FIG_DIR / 'combined_results_monochrome.png'
plt.savefig(fig2_path, dpi=300, bbox_inches='tight')
plt.close()
print('Saved:', fig2_path)

# Also copy over to report directory
import shutil
shutil.copyfile(fig1_path, REPORT_DIR / "figure2_utility_and_lifecycle.png")
shutil.copyfile(fig2_path, REPORT_DIR / "figure1_persistence_matrix.png")
print("Synced to report/ directory.")

