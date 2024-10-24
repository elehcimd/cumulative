from sklearn.datasets import load_iris

from cumulative.datasets.load_sklearn import load_sklearn
from cumulative.plotting import plot_ctx

c = load_sklearn(load_iris)
c.sample(m=100)

print("Dataset sample:")
print(c.df.head(5))
print("--\n")

print("Dataset overview:")
c.describe()
print("--\n")

c.score(src="base.z", dst="score", method="value")
c.sort(by="score.value")
c.interpolate(method="pchip", num=100)

with plot_ctx() as ax:
    c.plot.draw(ax=ax, src="base", style="-", ms=1, alpha=0.5, score="score.value")
