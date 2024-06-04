import pandas as pd
from cumulative import Cumulative
from cumulative.options import options


def test_default_fields():

    df = pd.DataFrame({
        "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
        "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
    })

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y", dst="test")

    # Test expected fields
    expected = [
        "idx",
        "test.name",
        "test.x",
        "test.y",
        "test.min",
        "test.max",
        "test.len",
        "test.sum",
        "test.len_zero",
        "test.len_negative",
        "test.len_positive",
    ]
    assert set(c.df.columns) == set(expected)


def test_attributes():

    df = pd.DataFrame({
        "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
        "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
        "category": ["A", "A", "A", "A", "A", "B", "B", "B", "B", "B"],
    })

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y", agg={"category": "first"})

    dst = options.get("transforms.destination")
    attributes = options.get("transforms.sequence.attributes")

    # Test presence of attribute column "category"
    assert f"{dst}.{attributes}.category" in c.df.columns
