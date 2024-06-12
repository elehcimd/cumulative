import matplotlib
import matplotlib as mpl
import pandas as pd
from matplotlib import pyplot as plt

from cumulative.opts import options


class Canvas:
    """
    Defines the drawing area in terms of matplotlib config, colors and preferences.
    """

    def __init__(self, x_label: str = "X", y_label: str = "Y", interactive: bool = True):
        """
        Initializes canvas with X,Y labels, in `interactive` mode on/off.
        """

        mpl.rcParams.update(mpl.rcParamsDefault)
        plt.rcParams["font.family"] = "monospace"
        cmap = matplotlib.colormaps["cool"]

        if interactive:
            plt.ion()
        else:
            plt.ioff()

        fig, ax = plt.subplots(figsize=(5, 5))

        ax.clear()
        ax.set_facecolor("black")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        lim_pad = 0.05
        ax.set_xlim(0 - lim_pad, 1 + lim_pad)
        ax.set_ylim(0 - lim_pad, 1 + lim_pad)

        self.fig = fig
        self.ax = ax
        self.cmap = cmap
        self.pen_color = "white"


class Plot:
    def __init__(self, c):
        """
        Initializes the plotting interface for the `c` Cumulative instance.
        """
        self.c = c

    def render(self, to: str = ""):
        """
        Draw what's on the canvas.
        """

        if to is None:
            if plt.isinteractive():
                plt.show()
        else:
            if to.endswith(".svg"):
                plt.savefig(to, format="svg")

    def xrays(
        self,
        src: str | None = None,
        canvas: Canvas | None = None,
        alpha: float = 1,
        ms: float = 1,
        lw: float = 1,
        k: int = 20,
        style: str = "-",
    ):
        """
        Simplifies the `src` prefix interpolating on `k` points, and renders them as monochrome points/curves.
        """

        src = options().default_if_null(src, "transforms.src")
        tmp = options().get("transforms.tmp")

        with options().ctx(
            {
                "transforms": {
                    "src": src,
                    "dst": tmp,
                    "drop": True,
                }
            }
        ):

            self.c.interpolate(src=src, method="pchipp", k=k, num=k)
            self.c.plot.scatter(canvas=canvas, alpha=alpha, ms=ms, lw=lw, style=style)
            self.c.drop(src=tmp)
            return self

    def scatter(
        self,
        src: str | None = None,
        canvas: Canvas | None = None,
        style: str = ".",
        ms: float = 2,
        lw: float = 1,
        score: str | None = None,
        alpha: str | None = 0.5,
        x_label: str = "X",
        y_label: str = "Y",
        color=None,
    ):

        src = options().default_if_null(src, "transforms.src")

        if canvas is None:
            canvas = Canvas(x_label=x_label, y_label=y_label)

        if color is None:
            color = canvas.pen_color

        for _, row in self.c.df.iterrows():
            row_color = canvas.cmap(row[score]) if isinstance(score, str) else color
            row_alpha = row[alpha] if isinstance(alpha, str) else alpha
            pd.Series(row[f"{src}.y"], index=row[f"{src}.x"]).plot(
                style=style,
                lw=lw,
                ms=ms,
                color=row_color,
                alpha=row_alpha,
                ax=canvas.ax,
            )

        return self
