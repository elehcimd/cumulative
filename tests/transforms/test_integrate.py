import pandas as pd
from cumulative import Cumulative


def test_default_fields():

    df = pd.DataFrame({
        "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
        "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
    })

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y")
    c.integrate(dst="test")

    # Test expected fields
    expected = ["test.x", "test.y"]
    assert set(c.columns_with_prefix("test")) == set(expected)
