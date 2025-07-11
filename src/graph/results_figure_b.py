import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Category labels
labels = ['L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'Q0', 'Q1', 'Q2', 'M0', 'M1', 'M2', 'G0', 'G1', 'G2']
x = np.arange(len(labels))

# Offsets and sizes
tight_offset = 0.15
merged_box_width = 0.3
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
p_center = np.array([0.9304, 0.8162, 0.8792, 0.6820, 0.5439, 0.7829, 0.6270, 0.7413, 0.7163, 0.7829, 0.7970, 0.6401, 0.7970, 0.6469, 0.7681])
p_low =    np.array([0.8855, 0.7448, 0.8199, 0.5953, 0.4509, 0.7066, 0.5369, 0.6600, 0.6326, 0.7066, 0.7227, 0.5507, 0.7227, 0.5578, 0.6899])
p_high =   np.array([0.9754, 0.8876, 0.9385, 0.7686, 0.6368, 0.8592, 0.7171, 0.8226, 0.8001, 0.8592, 0.8713, 0.7295, 0.8713, 0.7359, 0.8463])

r_best_center = np.array([0.4678, 0.3263, 0.3391, 0.5579, 0.2491, 0.3134, 0.3263, 0.2104, 0.2877, 0.3134, 0.2877, 0.2748, 0.2877, 0.2104, 0.1976])
r_best_low =    np.array([0.3747, 0.2390, 0.2510, 0.4653, 0.1688, 0.2271, 0.2390, 0.1351, 0.2035, 0.2271, 0.2035, 0.1919, 0.2035, 0.1351, 0.1241])
r_best_high =   np.array([0.5609, 0.4135, 0.4273, 0.6506, 0.3293, 0.3997, 0.4135, 0.2858, 0.3718, 0.3997, 0.3718, 0.3577, 0.3718, 0.2858, 0.2711])

r_worst_center = np.array([0.4164, 0.2748, 0.3005, 0.5450, 0.1590, 0.2748, 0.2619, 0.1718, 0.2104, 0.2491, 0.1718, 0.1718, 0.2362, 0.1847, 0.1590])
r_worst_low =    np.array([0.3244, 0.1919, 0.2153, 0.4521, 0.0918, 0.1919, 0.1803, 0.1024, 0.1351, 0.1688, 0.1024, 0.1024, 0.1575, 0.1132, 0.0918])
r_worst_high =   np.array([0.5083, 0.3577, 0.3858, 0.6379, 0.2261, 0.3577, 0.3435, 0.2413, 0.2858, 0.3293, 0.2413, 0.2413, 0.3149, 0.2563, 0.2261])

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
  r_best_low, r_best_center, r_best_high,
  r_worst_low, r_worst_center, r_worst_high
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
    ax.plot(pos, cmn, marker='o', color=worst_color, markersize=5)
    ax.plot(pos, cmx, marker='o', color=best_color, markersize=5)
  ax.plot([], [], color=box_color, linewidth=8, label=label)

# Draw plots
draw_boxes(ax, merged_left, merged_p_low, merged_p_cmin, merged_p_cmax, merged_p_high, precision_color, 'Precision CI')
draw_boxes(ax, merged_right, merged_r_low, merged_r_cmin, merged_r_cmax, merged_r_high, recall_color, 'Recall CI')

# Legend setup
legend_handles = [
  Line2D([0], [0], color=precision_color, linewidth=8, label='Precision CI'),
  Line2D([0], [0], color=recall_color, linewidth=8, label='Recall CI'),
  Line2D([0], [0], marker='o', color='w', markerfacecolor=best_color, markersize=6, label='Best Average'),
  Line2D([0], [0], marker='o', color='w', markerfacecolor=worst_color, markersize=6, label='Worst Average'),
]

ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('Score')
ax.set_ylim(0, 1.05)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(handles=legend_handles, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4, frameon=False)

plt.tight_layout()
plt.savefig("../../results/graph/results_figure_b.png", dpi=300)
#plt.show()
