import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.style.use("/Users/wmd122/github/wedap/wedap/styles/default.mplstyle")

# Define legend entries
legend_elements = [
    Line2D([0], [0], color='red', lw=2, label='Hydrogen Bonding'),
    Line2D([0], [0], color='green', lw=2, label='Hydrophobic Interactions'),
    Line2D([0], [0], color='blue', lw=2, label='Electrostatic Interactions'),
]

# Create a figure just for the legend
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center', frameon=False, fontsize=12)
ax.axis('off')  # Hide axes

plt.savefig('legend.pdf', bbox_inches='tight')
plt.show()

