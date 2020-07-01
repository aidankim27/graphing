import numpy as np
import matplotlib.pyplot as plt


korea = (
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,],
    [18, 22, 28, 34, 35, 42, 44, 50, 51, 54],
)

wuhan = (
    [3, 4, 5, 6, 7, 8, 9,],
    [2282, 2305, 2328, 2349, 2370, 2388, 2404],
)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fig, ax1 = plt.subplots()

color = "tab:red"
ax1.set_ylabel("Korean Deaths", color=color)
ax1.tick_params(axis="y", labelcolor=color)
plt1 = plt.plot(*korea, marker="8", linestyle="-", color="r", label="Korea Deaths ")
ax1.set_xlabel("Date(March)", color="black")
ax2 = ax1.twinx()

color = "tab:blue"
ax2.set_ylabel("Wuhan Deaths", color=color)
ax2.tick_params(axis="y", labelcolor=color)
plt2 = plt.plot(*wuhan, marker="o", linestyle="--", color="b", label="Wuhan Deaths ")
fig.tight_layout()

plt.title("COVID-19 Deaths: S.Korea vs Wuhan, China ")
plt.show()
