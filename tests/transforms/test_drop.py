import pandas as pd
from cumulative import Cumulative


def test_copy():

    df = pd.DataFrame({
        "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        "x": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
        "y": [10, 20, 30, 40, 50, 100, 200, 300, 400, 500],
    })

    c = Cumulative(df_raw=df).sequence(group="id", x="x", y="y")

    c.copy(dst="test")

    # Test presence of destination column
    assert "test.x" in c.df.columns

    # Add one more column with no "."
    c.df["test"] = 123

    # Remove columns "test", "test.*"
    c.drop(src="test")

    # Test that all tet columns have been removed
    assert len([col for col in c.df.columns if col.startswith("test")]) == 0
