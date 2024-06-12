from cumulative.datasets.load_twoseries import load_twoseries


def test_load_twoseries():
    """
    Test: We can load a dataset of two series with varying length.
    """

    c = load_twoseries()
    c.copy(dst="test")
    assert c.df.iloc[0]["test.x"] == [0, 1, 2, 3, 4, 5]
    assert c.df.iloc[1]["test.x"] == [0, 1, 2, 3]
