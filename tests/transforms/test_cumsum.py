import numpy as np

from cumulative.datasets.load_wide import load_wide


def test_cumsum_y():

    c = load_wide()
    c.cumsum(dst="test")
    row = c.df.iloc[0]
    np.testing.assert_allclose(np.cumsum(row["base.y"]), row["test.y"])


def test_cumsum_xy():

    c = load_wide()
    c.cumsum(dst="test", kind="xy")
    row = c.df.iloc[0]
    np.testing.assert_allclose(np.cumsum(row["base.x"]), row["test.x"])
    np.testing.assert_allclose(np.cumsum(row["base.y"]), row["test.y"])
