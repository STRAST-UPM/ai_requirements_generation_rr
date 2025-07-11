import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

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
  'font.size': 18,
  'axes.labelsize': 20,
  'xtick.labelsize': 16,
  'ytick.labelsize': 16,
  'legend.fontsize': 18
})

# Plotting function for aligned dumbbells with larger dots
def draw_aligned_dumbbells(ax, positions, low, high, line_color, low_color, high_color, label):
  for x_pos, lo, hi in zip(positions, low, high):
    ax.plot([x_pos, x_pos], [lo, hi], color=line_color, linewidth=1.5)
    ax.plot(x_pos, lo, marker='o', color=low_color, markersize=7)
    ax.plot(x_pos, hi, marker='o', color=high_color, markersize=7)
  ax.plot([], [], color=line_color, marker='o', markerfacecolor=high_color,
      markeredgecolor=line_color, linestyle='None', label=label)

# Create the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Draw dumbbells
draw_aligned_dumbbells(ax, x, f2_worst, f2_best, 'black', '#1f77b4', '#1f77b4', 'F2')
draw_aligned_dumbbells(ax, x, f2s_worst, f2s_best, 'black', '#ff7f0e', '#ff7f0e', 'F2-synthetic')

# Formatting axes
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('F2 Score')
ax.set_ylim(0, 1.05)
ax.grid(True, linestyle='--', alpha=0.5)

# Custom legend
f2_patch = mpatches.Patch(color='#1f77b4', label='F2')
f2s_patch = mpatches.Patch(color='#ff7f0e', label='Uplift F2')
ax.legend(handles=[f2_patch, f2s_patch], loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)

# Save and display
plt.tight_layout()
plt.savefig("../../results/graph/results_figure_a.png", dpi=300)
#plt.show()
