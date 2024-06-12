from cumulative.datasets.load_wide import load_wide


def test_scale_xy():

    c = load_wide()
    c.scale(dst="test", kind="xy")
    row = c.df.iloc[0]
    assert row["test.x"].min() == 0
    assert row["test.x"].max() == 1
    assert row["test.y"].min() == 0
    assert row["test.y"].max() == 1


def test_scale_x():

    c = load_wide()
    c.scale(dst="test", kind="x")

    assert set(c.frame("test").columns.tolist()) == {"test.x", "test.x.min", "test.x.max", "test.y"}

    row = c.df.iloc[0]
    assert row["test.x"].min() == 0
    assert row["test.x"].max() == 1


def test_scale_y():

    c = load_wide()
    c.scale(dst="test", kind="y")

    assert set(c.frame("test").columns.tolist()) == {"test.x", "test.y.min", "test.y.max", "test.y"}

    row = c.df.iloc[0]
    assert row["test.y"].min() == 0
    assert row["test.y"].max() == 1
