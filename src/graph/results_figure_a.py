import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
from matplotlib.ticker import MultipleLocator

# Labels for the categories
labels = ['L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'Q0', 'Q1', 'Q2', 'M0', 'M1', 'M2', 'G0', 'G1', 'G2']
x = np.arange(len(labels))

# F2 and F2-synthetic worst/best values
f2_worst = np.array([0.45, 0.47, 0.31, 0.34, 0.57, 0.17, 0.31, 0.29, 0.19, 0.23, 0.28, 0.19, 0.19, 0.26, 0.20, 0.18])
f2_best = np.array([0.45, 0.52, 0.36, 0.38, 0.58, 0.27, 0.35, 0.36, 0.23, 0.32, 0.35, 0.32, 0.30, 0.32, 0.23, 0.22])
f2s_worst = np.array([1.00, 0.96, 0.79, 0.86, 0.76, 0.50, 0.76, 0.63, 0.64, 0.66, 0.75, 0.67, 0.57, 0.74, 0.59, 0.64])
f2s_best = np.array([1.00, 0.98, 0.82, 0.88, 0.77, 0.56, 0.79, 0.66, 0.68, 0.72, 0.79, 0.78, 0.65, 0.78, 0.61, 0.69])

# Font config
plt.rcParams.update({
  'font.family': 'Times New Roman',
  'font.size': 27,
  'axes.labelsize': 27,
  'xtick.labelsize': 27,
  'ytick.labelsize': 27,
  'legend.fontsize': 27
})

# Plotting function for aligned dumbbells with larger dots
def draw_aligned_dumbbells(ax, positions, low, high, line_color, low_color, high_color, label):
  for x_pos, lo, hi in zip(positions, low, high):
    ax.plot([x_pos, x_pos], [lo, hi], color=line_color, linewidth=1.5)
    ax.plot(x_pos, lo, marker='o', color=low_color, markersize=9, clip_on=False)
    ax.plot(x_pos, hi, marker='o', color=high_color, markersize=9, clip_on=False)
  ax.plot([], [], color=line_color, marker='o', markerfacecolor=high_color,
      markeredgecolor=line_color, linestyle='None', label=label)

# Create the figure
fig, ax = plt.subplots(figsize=(12, 7.5))

# Draw dumbbells
draw_aligned_dumbbells(ax, x, f2_worst, f2_best, 'black', '#1f77b4', '#1f77b4', 'F2')
draw_aligned_dumbbells(ax, x, f2s_worst, f2s_best, 'black', '#ff7f0e', '#ff7f0e', 'F2-synthetic')

# Formatting axes
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('F2 score', ha='left', x=1.0)
ax.set_xlabel('Model config.', ha='right', x=1.0)
ax.set_ylim(0, 1.00)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_yticks(np.arange(0, 1.01, 0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.grid(which='minor', axis='y', linestyle='--', alpha=0.5)
ax.grid(which='major', axis='y', linestyle='--', alpha=0.5)

# Custom legend
f2_patch = mpatches.Patch(color='#1f77b4', label='F2')
f2s_patch = mpatches.Patch(color='#ff7f0e', label='Relative F2')
ax.legend(
  handles=[
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#1f77b4', markersize=14, label='F2\n(best/worst)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#ff7f0e', markersize=14, label='Relative F2\n(best/worst)'),
  ],
  loc='upper center', bbox_to_anchor=(0.25, -0.25), ncol=2, frameon=False
)

# Save and display
plt.tight_layout()
plt.savefig("../../results/graph/results_figure_a.png", dpi=300)
plt.show()
