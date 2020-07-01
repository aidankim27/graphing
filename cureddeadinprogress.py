import numpy as np
import matplotlib.pyplot as plt


n_bins = 3
fig, ax = plt.subplots()
x = ([9, 9.5, 10,], [105687, 109577, 113702,])

ax.hist(x, n_bins, density=True, histtype="bar", stacked=True)
ax.set_title("stacked bar")


fig.tight_layout()
plt.show()
