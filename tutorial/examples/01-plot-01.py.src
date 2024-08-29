from scipy.stats import cosine

from cumulative.datasets.load_dist import load_dist

c = load_dist([cosine] * 100, kind="rvs")

print("Dataset overview:")
c.describe()

c.plot.scatter(style="-", color="blue", alpha=0.1).render()
