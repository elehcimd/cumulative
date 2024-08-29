import numpy as np
import pandas as pd

from cumulative.loaders.preprocess import melt, nest


def test_melt():
    """
    Test: We can melt a table representing time series to long format.
    """

    df = pd.DataFrame(
        {
            "id": ["S1", "S2", "S3"],
            "category": ["A", "A", "B"],
            "t1": [5, 10, 5],
            "t2": [10, 15, 10],
            "t3": [30, 35, 15],
            "t4": [50, 55, 20],
            "t5": [20, 60, 25],
        }
    )

    df = melt(df, group="id", attributes=["category"])

    assert df.columns.tolist() == ["c", "x", "y", "name", "attr.category"]


def test_nest():
    """
    Test: We can aggregate a table of time series in long format to nested format.
    """

    df = pd.DataFrame(
        {
            "id": ["S1", "S2", "S3"],
            "category": ["A", "A", "B"],
            "t1": [5, 10, 5],
            "t2": [10, 15, 10],
            "t3": [30, 35, 15],
            "t4": [50, 55, 20],
            "t5": [20, 60, 25],
        }
    )

    df = melt(df, group="id", attributes=["category"])
    df = nest(df)

    print(df.columns.tolist())
    assert df.columns.tolist() == ["base.name", "base.c", "base.x", "base.y", "base.attr.category"]

    assert df.iloc[0]["base.x"].dtype == np.dtype("float64")
    assert df.iloc[0]["base.y"].dtype == np.dtype("float64")
