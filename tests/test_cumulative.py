import pandas as pd
from cumulative import Cumulative


def test_cumulative():

    df = pd.DataFrame(
        {
            "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
            "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
        }
    )

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y", dst="sequence")

    # two series loaded correctly
    assert len(c.df) == 2

    # Test the correct loading of a simple dataset
    assert "idx" in c.df.columns
    assert "sequence.x" in c.df.columns
    assert "sequence.y" in c.df.columns
    assert "sequence.name" in c.df.columns
