from cumulative.datasets.load_dist import load_dist
from cumulative.plot import Canvas
from scipy.stats import norm

canvas = Canvas()
load_dist([norm(0, 1)] * 30, kind="rvs").plot.scatter(canvas=canvas, style="-", color="green", alpha=0.5)
load_dist([norm(0, 2)] * 30, kind="rvs").plot.scatter(canvas=canvas, style="-", color="blue", alpha=0.5)
load_dist([norm(0, 3)] * 30, kind="rvs").plot.scatter(canvas=canvas, style="-", color="red", alpha=0.5).render()
