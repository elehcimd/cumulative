import pandas as pd
from cumulative import Cumulative


def test_default_fields():

    df = pd.DataFrame(
        {
            "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
            "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
        }
    )

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y")
    c.scale(dst="test")

    # Test expected fields
    expected = ["test.x_min", "test.x_max", "test.y_min", "test.y_max", "test.x", "test.y"]
    assert set(c.columns_with_prefix("test")) == set(expected)


def test_x_min():

    df = pd.DataFrame(
        {
            "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
            "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
        }
    )

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y", dst="seq")
    c.scale(src="seq", dst="test")

    # Test y_min value for id=2
    assert c.df[c.df["seq.name"] == 2]["test.y_min"].iloc[0] == 100
