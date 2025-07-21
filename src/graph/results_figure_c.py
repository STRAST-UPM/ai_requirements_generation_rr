import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Category labels
labels = ['L0', 'E0', 'E1', 'E2', 'E3', 'E4']
x = np.arange(len(labels))

# Offsets and sizes
tight_offset = 0.1
merged_box_width = 0.2
half_merged = merged_box_width / 2
merged_left = x - tight_offset
merged_right = x + tight_offset
solid_alpha_final = 1.0

# Colors
precision_color = '#1f77b4'  # Blue
recall_color = '#2ca02c'     # Green
best_color = '#ff7f0e'       # Orange
worst_color = '#d62728'      # Red
line_color = 'black'

# Font config
plt.rcParams.update({
  'font.family': 'Times New Roman',
  'font.size': 18,
  'axes.labelsize': 20,
  'xtick.labelsize': 16,
  'ytick.labelsize': 16,
  'legend.fontsize': 18
})

# Actual data (could be loaded from file)
p_center = np.array([0.9304, 0.7377, 0.4511, 0.7005, 0.8217, 0.8690])
p_low =    np.array([0.8855, 0.6560, 0.3583, 0.6153, 0.7512, 0.8075])
p_high =   np.array([0.9754, 0.8193, 0.5440, 0.7856, 0.8922, 0.9306])

r_center = np.array([0.4421, 0.6609, 0.9311, 0.6094, 0.4678, 0.4035])
r_low =    np.array([0.3495, 0.5727, 0.8864, 0.5184, 0.3747, 0.3120])
r_high =   np.array([0.5346, 0.7490, 0.9758, 0.7003, 0.5609, 0.4950])

# Merge using extremes
def merge_extremes(low1, center1, high1, low2, center2, high2):
  return (
    np.minimum(low1, low2),
    np.minimum(center1, center2),
    np.maximum(center1, center2),
    np.maximum(high1, high2)
  )

merged_p_low, merged_p_cmin, merged_p_cmax, merged_p_high = merge_extremes(
  p_low, p_center, p_high,
  p_low, p_center, p_high
)

merged_r_low, merged_r_cmin, merged_r_cmax, merged_r_high = merge_extremes(
  r_low, r_center, r_high,
  r_low, r_center, r_high
)

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

def draw_boxes(ax, positions, low, cmin, cmax, high, box_color, label):
  for i, (pos, lo, cmn, cmx, hi) in enumerate(zip(positions, low, cmin, cmax, high)):
    ax.add_patch(plt.Rectangle((pos - half_merged, min(lo, cmn)), merged_box_width, abs(cmn - lo),
                   color=box_color, alpha=solid_alpha_final, linewidth=0))
    ax.add_patch(plt.Rectangle((pos - half_merged, min(cmn, cmx)), merged_box_width, abs(cmx - cmn),
                   color=box_color, alpha=solid_alpha_final, linewidth=0))
    ax.add_patch(plt.Rectangle((pos - half_merged, min(cmx, hi)), merged_box_width, abs(hi - cmx),
                   color=box_color, alpha=solid_alpha_final, linewidth=0))
    ax.plot([pos, pos], [cmn, cmx], color=line_color, linewidth=1.5)
    ax.plot(pos, cmx, marker='o', color=best_color, markersize=5)
  ax.plot([], [], color=box_color, linewidth=8, label=label)

# Draw plots
draw_boxes(ax, merged_left, merged_p_low, merged_p_cmin, merged_p_cmax, merged_p_high, precision_color, 'Precision CI')
draw_boxes(ax, merged_right, merged_r_low, merged_r_cmin, merged_r_cmax, merged_r_high, recall_color, 'Recall CI')

# Legend setup
legend_handles = [
  Line2D([0], [0], color=precision_color, linewidth=8, label='Precision CI'),
  Line2D([0], [0], color=recall_color, linewidth=8, label='Recall CI'),
  Line2D([0], [0], marker='o', color='w', markerfacecolor=best_color, markersize=6, label='Average'),
]

ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('Score')
ax.set_ylim(0, 1.05)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(handles=legend_handles, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4, frameon=False)

plt.tight_layout()
plt.savefig("../../results/graph/results_figure_c.png", dpi=300)
plt.show()
