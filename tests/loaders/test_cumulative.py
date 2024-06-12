import pandas as pd
from cumulative.datasets.load_wide import load_wide


def test_cumulative():
    """
    Test: We can load instantiate the Cumulative class on a well formatted data frame.
    """

    c = load_wide()

    assert isinstance(c.df, pd.DataFrame)
    assert "base.x" in c.df.columns
