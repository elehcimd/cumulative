import numpy as np
import pandas as pd

from cumulative.datasets.load_wide import load_wide
from cumulative.transforms.transform import Transform


def test_register_transform():
    """
    Test: We can register a custom row transform.
    """

    c = load_wide()

    # Define, register and execute a custom transform
    class TestTransform(Transform):
        def transform_row(self, row, src, **kwargs):
            return pd.Series({"result": np.sum(row[f"{src}.y"])})

    c.register_transform("test_transform", TestTransform)

    c.test_transform(dst="test")

    assert c.df["test.result"].sum() == 365.0
    assert "test.result" in c.df.columns
