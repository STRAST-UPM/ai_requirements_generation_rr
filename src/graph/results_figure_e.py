import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# cumulative counts data
true_support=[
  14.5,0,1,10,0,1,9.5,5,0,3,4,7,1,7.5,7,7,4,9.5,0,9.5,3.5,1,5,2,3,3,1,1,1,1,1,2,1,
  14.5,5.5,4,1,2,3,14.5,1,1,2,
  10,6.5,5,1,7,2,1,1,1,1,2,
  15,2,1,
  13.5,4,13.5,2,1,5,2,1,
  5.5,7.5,10.5,1,4,2,1,2,1,1
]
hall_support=[1,3,1,1,1,4,1,1,2,2,1,1,1,1,1,4,4,8,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,3,1,1,1,1,2,2,2,3,1,1]

max_n=15
ns=np.arange(1,max_n+1)
cum_true=[sum(1 for v in true_support if v>=n) for n in ns]
cum_hall=[sum(1 for v in hall_support if v>=n) for n in ns]

plt.rcParams.update({
  'font.family': 'Times New Roman',
  'font.size': 18,
  'axes.labelsize': 20,
  'xtick.labelsize': 16,
  'ytick.labelsize': 16,
  'legend.fontsize': 18
})

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(ns, cum_true, marker='o', linewidth=2, color='#1f77b4')
ax.plot(ns, cum_hall, marker='o', linewidth=2, color='#d62728')
ax.set_xticks(ns)
ax.set_ylabel('Number of items')
ax.grid(True, linestyle='--', alpha=0.5)

valid_patch = mpatches.Patch(color='#1f77b4', label='Valid requirements')
hall_patch = mpatches.Patch(color='#d62728', label='Hallucinations')
ax.legend(handles=[valid_patch, hall_patch], loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False)

plt.tight_layout()
plt.savefig("../../results/graph/results_figure_e.png", dpi=300)
plt.show()
