from cumulative.datasets.load_dist import load_dist
from scipy.stats import cosine

c = load_dist([cosine(1, 2)] * 300, kind="rvs").scale(kind="xy")

print("Dataset overview:")
c.describe()

c.plot.scatter(style="-", color="white", alpha=0.1).render()
