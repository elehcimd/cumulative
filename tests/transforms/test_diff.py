import numpy as np
from cumulative.datasets.load_wide import load_wide


def test_diff_y():

    c = load_wide().cumsum(dst="int")
    c.diff(src="int", dst="der")
    row = c.df.iloc[0]
    np.testing.assert_allclose(row["der.y"], row["base.y"])
