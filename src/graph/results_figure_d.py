import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Data arrays
labels = ['L0', 'E0', 'E1', 'E2', 'E3', 'E4']
precision_c = np.array([0.9304, 0.7377, 0.4511, 0.7005, 0.8217, 0.8690])
precision_low = np.array([0.8855, 0.6560, 0.3583, 0.6153, 0.7512, 0.8075])
precision_high = np.array([0.9754, 0.8193, 0.5440, 0.7856, 0.8922, 0.9306])

recall_c = np.array([0.4421, 0.6609, 0.9311, 0.6094, 0.4678, 0.4035])
recall_low = np.array([0.3495, 0.5727, 0.8864, 0.5184, 0.3747, 0.3120])
recall_high = np.array([0.5346, 0.7490, 0.9758, 0.7003, 0.5609, 0.4950])

plt.rcParams.update({'font.family':'Times New Roman','font.size':14})

fig, ax = plt.subplots(figsize=(7,6))

# CI rectangles and points
for i, lbl in enumerate(labels):
  w = precision_high[i]-precision_low[i]
  h = recall_high[i]-recall_low[i]
  ax.add_patch(plt.Rectangle((precision_low[i], recall_low[i]), w, h,
                              alpha=0.3, color='#d3d3d3'))
  ax.plot(precision_c[i], recall_c[i], 'o', markersize=6, color='black')
  ax.text(precision_c[i]+0.005, recall_c[i]+0.005, lbl)

ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_xlim(0.3,1.0)
ax.set_ylim(0.3,1.0)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("../../results/graph/results_figure_d.png", dpi=300)
plt.show()