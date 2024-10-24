from scipy.stats import norm

from cumulative.datasets.load_dist import load_dist
from cumulative.plotting import plot_ctx

with plot_ctx() as ax:
    load_dist([norm(0, 1)] * 30, kind="rvs").plot.draw(ax=ax, style="-", color="green", alpha=0.5)
    load_dist([norm(0, 2)] * 30, kind="rvs").plot.draw(ax=ax, style="-", color="blue", alpha=0.5)
    load_dist([norm(0, 3)] * 30, kind="rvs").plot.draw(ax=ax, style="-", color="red", alpha=0.5)
