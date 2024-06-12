import numpy as np
from cumulative.datasets.load_wide import load_wide


def test_apply():

    c = load_wide()
    c.apply(dst="test", func=lambda s: {"z": np.cumsum(s["x"])})
    row = c.df.iloc[0]
    assert row["test.z"].tolist() == [1, 3, 6, 10, 15]
