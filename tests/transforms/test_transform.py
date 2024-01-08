import numpy as np
import pandas as pd
from cumulative import Cumulative
from cumulative.options import options
from cumulative.transforms.transform import Transform


def test_dst():

    df = pd.DataFrame({
        "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
        "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
    })

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y")

    # Test default destination of transforms
    assert f"{options.get('transforms.destination')}.x" in c.df.columns

    # Test default source of transforms
    # Test custom destination of transforms
    c.copy(dst="test1")
    assert "test1.x" in c.df.columns

    # Test custom source and destination of transforms
    c.copy(src="test1", dst="test2")
    assert "test2.x" in c.df.columns


def test_register_transform():

    df = pd.DataFrame({
        "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
        "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
    })

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y")

    # Define, register and execute a custom transform
    class TestTransform(Transform):
        def transform_row(self, row, src, **kwargs):
            return pd.Series({"result": np.sum(row[f"{src}.y"])})

    c.register_transform("test_transform", TestTransform)

    c.test_transform(dst="test")

    # Test that there's a newly created column named "test.result"
    assert "test.result" in c.df.columns
