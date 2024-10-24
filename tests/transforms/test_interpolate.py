import numpy as np

from cumulative.datasets.load_wide import load_wide


def test_interpolate_interp():
    c = load_wide()
    c.interpolate(num=3, dst="int")
    row = c.df.iloc[0]
    assert row["int.model.name"] == "interp"
    np.testing.assert_allclose(row["int.x"], [1.0, 3.0, 5.0])
    np.testing.assert_allclose(row["int.y"], [5.0, 12.5, 20.0])


def test_interpolate_pchip():
    c = load_wide().cumsum()
    c.interpolate(method="pchip", num=3, dst="int")
    row = c.df.iloc[0]
    assert row["int.model.name"] == "pchip"
    print(row)


def test_interpolate_pchipp():
    c = load_wide().cumsum()
    c.interpolate(method="pchipp", num=3, dst="int")
    row = c.df.iloc[0]
    assert row["int.model.name"] == "pchipp"
    print(row)
