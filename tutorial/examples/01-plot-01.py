from scipy.stats import cosine

from cumulative.datasets.load_dist import load_dist
from cumulative.plotting import plot_ctx

c = load_dist([cosine] * 100, kind="rvs")

print("Dataset overview:")
c.describe()

with plot_ctx() as ax:
    c.plot.draw(ax=ax, style="-", color="blue", alpha=0.1)
