import numpy as np
import matplotlib.pyplot as plt

cases = [
    11953,
    14557,
    17391,
    20630,
    24554,
    28276,
    31481,
    34886,
    37558,
    40554,
    43103,
    45171,
    46997,
    49053,
    50580,
    51857,
    71429,
    73332,
    75204,
    75748,
    76769,
    77794,
    78811,
    79331,
    81109,
    82294,
    83652,
    85403,
]

dead = [
    259,
    305,
    426,
    490,
    492,
    565,
    638,
    724,
    813,
    910,
    1018,
    1115,
    1369,
    1383,
    1526,
    1669,
    1775,
    1873,
    2009,
    2129,
    2247,
    2359,
    2452,
    2618,
    2761,
    2804,
    2858,
    2924,
]
fig, ax1 = plt.subplots()

color = "tab:red"
ax1.set_ylabel("cases", color=color)
ax1.tick_params(axis="y", labelcolor=color)
plt.plot(*cases, marker="8", linestyle="-", color="r", label="Cases ")
ax1.set_xlabel("Date(Feb)", color="black")

ax2 = ax1.twinx()

color = "tab:blue"
ax2.set_ylabel("dead", color=color)
ax2.tick_params(axis="y", labelcolor=color)
plt.plot(*dead, marker="o", linestyle="--", color="b", label="Dead ")
fig.tight_layout()


plt.title("COVID-19 Death: Cases to Death")
plt.show()
