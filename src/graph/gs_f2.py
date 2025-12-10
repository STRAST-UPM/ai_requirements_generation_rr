import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
from matplotlib.legend_handler import HandlerTuple

# Category labels
labels = ['L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'Q0', 'Q1', 'Q2', 'M0', 'M1', 'M2', 'G0', 'G1', 'G2']
x = np.arange(len(labels))

# Offsets and sizes
tight_offset = 0.15
merged_box_width = 0.3
half_merged = merged_box_width / 2
merged_left = x - tight_offset
merged_right = x + tight_offset
box_alpha = 1.0

# Colors

# precision is light blue, recall is light green
# centers are darker versions of the same colors

precision_color = '#99ddff'
recall_color = '#99ff9c'
precision_center_color = "#006699"
recall_center_color = "#009900"
line_color = 'black'

# Font config
plt.rcParams.update({
  'font.family': 'Times New Roman',
  'font.size': 27,
  'axes.labelsize': 27,
  'xtick.labelsize': 27,
  'ytick.labelsize': 27,
  'legend.fontsize': 27
})

# Actual data (could be loaded from file)
p_center = np.array([0.9320, 0.7897, 0.8794, 0.6317, 0.5439, 0.7830, 0.5966, 0.7414, 0.7164, 0.7830, 0.7414, 0.6024, 0.7971, 0.5966, 0.7287])
p_low =    np.array([0.8878, 0.7148, 0.8204, 0.5424, 0.4516, 0.7073, 0.5057, 0.6607, 0.6332, 0.7073, 0.6607, 0.5117, 0.7233, 0.5057, 0.6467])
p_high =   np.array([0.9762, 0.8646, 0.9383, 0.7210, 0.6362, 0.8588, 0.6875, 0.8221, 0.7997, 0.8588, 0.8221, 0.6931, 0.8709, 0.6875, 0.8107])

r_best_center = np.array([0.4746, 0.3221, 0.3348, 0.5508, 0.2459, 0.3094, 0.3221, 0.2078, 0.2840, 0.3094, 0.2840, 0.2713, 0.2840, 0.2078, 0.1951])
r_best_low =    np.array([0.3820, 0.2357, 0.2475, 0.4586, 0.1665, 0.2240, 0.2357, 0.1332, 0.2007, 0.2240, 0.2007, 0.1893, 0.2007, 0.1332, 0.1224])
r_best_high =   np.array([0.5672, 0.4085, 0.4221, 0.6430, 0.3252, 0.3949, 0.4085, 0.2823, 0.3673, 0.3949, 0.3673, 0.3533, 0.3673, 0.2823, 0.2678])

r_worst_center = np.array([0.4238, 0.2713, 0.2967, 0.5381, 0.1569, 0.2713, 0.2586, 0.1697, 0.2078, 0.2459, 0.1697, 0.1697, 0.2332, 0.1824, 0.1569])
r_worst_low =    np.array([0.3322, 0.1893, 0.2123, 0.4457, 0.0906, 0.1893, 0.1779, 0.1010, 0.1332, 0.1665, 0.1010, 0.1010, 0.1553, 0.1116, 0.0906])
r_worst_high =   np.array([0.5153, 0.3533, 0.3811, 0.6305, 0.2233, 0.3533, 0.3393, 0.2383, 0.2823, 0.3252, 0.2383, 0.2383, 0.3110, 0.2531, 0.2233])

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
fig, ax = plt.subplots(figsize=(12, 7.7))

def draw_boxes(ax, positions, low, cmin, cmax, high, box_color, label):
  for i, (pos, lo, cmn, cmx, hi) in enumerate(zip(positions, low, cmin, cmax, high)):
    ax.add_patch(plt.Rectangle((pos - half_merged, min(lo, cmn)), merged_box_width, abs(cmn - lo),
                   color=box_color, alpha=box_alpha, linewidth=0))
    ax.add_patch(plt.Rectangle((pos - half_merged, min(cmn, cmx)), merged_box_width, abs(cmx - cmn),
                   color=box_color, alpha=box_alpha, linewidth=0))
    ax.add_patch(plt.Rectangle((pos - half_merged, min(cmx, hi)), merged_box_width, abs(hi - cmx),
                   color=box_color, alpha=box_alpha, linewidth=0))
    ax.plot([pos, pos], [cmn, cmx], color=recall_center_color, linewidth=1.5)
  ax.plot([], [], color=box_color, linewidth=8, label=label)

# Draw plots
draw_boxes(ax, merged_left, merged_p_low, merged_p_cmin, merged_p_cmax, merged_p_high, precision_color, 'Precision CI')
draw_boxes(ax, merged_right, merged_r_low, merged_r_cmin, merged_r_cmax, merged_r_high, recall_color, 'Recall CI')
ax.plot(merged_left, merged_p_cmin, 'o', color=precision_center_color, markersize=7)
ax.plot(merged_left, merged_p_cmax, 'o', color=precision_center_color, markersize=7)
ax.plot(merged_right, merged_r_cmin, 'o', color=recall_center_color, markersize=7)
ax.plot(merged_right, merged_r_cmax, 'o', color=recall_center_color, markersize=7)

# Legend setup
legend_handles = [
  Line2D([0], [0], marker='o', color='w', markerfacecolor=precision_center_color, markersize=11, label='Precision'),
  Line2D([0], [0], marker='o', color='w', markerfacecolor=recall_center_color, markersize=11, label='Recall (best/worst)'),
  Line2D([0], [0], color=precision_color, linewidth=8, label='CI (90%)'),
  Line2D([0], [0], color=recall_color, linewidth=8, label='CI (90%)')
]

ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('Score', ha='left', x=1.0)
ax.set_xlabel('Model config.', ha='right', x=1.0)
ax.set_ylim(0, 1.00)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_yticks(np.arange(0, 1.01, 0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.grid(which='minor', axis='y', linestyle='--', alpha=0.5)
ax.grid(which='major', axis='y', linestyle='--', alpha=0.5)
ax.legend(
  handles=legend_handles,
  loc='upper center',
  bbox_to_anchor=(0.33, -0.25),
  ncol=2,
  frameon=False,
  handletextpad=0.35
)

plt.tight_layout()
plt.savefig("../../results/graph/results_figure_b.png", dpi=300)
#plt.show()
