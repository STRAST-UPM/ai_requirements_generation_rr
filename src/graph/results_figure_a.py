import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
from matplotlib.ticker import MultipleLocator
from matplotlib.legend_handler import HandlerBase

# Labels for the categories
labels = ['L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'Q0', 'Q1', 'Q2', 'M0', 'M1', 'M2', 'G0', 'G1', 'G2']
x = np.arange(len(labels))

# F2 and F2-synthetic worst/best values
f2_worst = np.array([0.46, 0.30, 0.33, 0.56, 0.17, 0.30, 0.28, 0.19, 0.23, 0.28, 0.19, 0.19, 0.26, 0.20, 0.17])
f2_best = np.array([0.51, 0.36, 0.38, 0.57, 0.27, 0.35, 0.35, 0.23, 0.32, 0.35, 0.32, 0.30, 0.32, 0.23, 0.22])
f2s_worst = np.array([1.01, 0.69, 0.76, 1.11, 0.39, 0.69, 0.63, 0.44, 0.53, 0.63, 0.44, 0.43, 0.60, 0.46, 0.41])
f2s_best = np.array([1.11, 0.80, 0.84, 1.13, 0.59, 0.77, 0.75, 0.54, 0.70, 0.77, 0.71, 0.65, 0.72, 0.52, 0.50])

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
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_yticks(np.arange(0, 1.21, 0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.grid(which='minor', axis='y', linestyle='--', alpha=0.5)
ax.grid(which='major', axis='y', linestyle='--', alpha=0.5)

# Custom handler to align marker with the first line of text
class HandlerDotAlignFirstLine(HandlerBase):
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        center = y0 + 1.3 * height  # shift up
        p = plt.Line2D([x0+40], [center],
                       linestyle='None',
                       marker='o',
                       markersize=14,
                       markerfacecolor=orig_handle.get_markerfacecolor(),
                       markeredgecolor='none',
                       transform=trans)
        return [p]

# Create dummy handles
f2_handle = Line2D([0], [0], marker='o', color='w',
                   markerfacecolor='#1f77b4', markersize=14,
                   label='F2\n(best/worst)')
f2s_handle = Line2D([0], [0], marker='o', color='w',
                    markerfacecolor='#ff7f0e', markersize=14,
                    label='Relative F2\n(best/worst)')

# Legend with custom handler
ax.legend(
    handles=[f2_handle, f2s_handle],
    handler_map={f2_handle: HandlerDotAlignFirstLine(),
                 f2s_handle: HandlerDotAlignFirstLine()},
    loc='upper center',
    bbox_to_anchor=(0.25, -0.25),
    ncol=2,
    frameon=False,
    handletextpad=0.5,  # reduce space between dot and text
    borderpad=0.4,
    columnspacing=1.0,
    labelspacing=1.0
)

# Save and display
plt.tight_layout()
plt.savefig("../../results/graph/results_figure_a.png", dpi=300)
#plt.show()
