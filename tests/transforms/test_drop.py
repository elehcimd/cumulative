from cumulative.datasets.load_wide import load_wide


def test_drop():
    """
    Test: We can drop columns by prefix.
    """

    c = load_wide()
    c.copy(dst="test")
    assert "test.x" in c.df.columns
    c.drop(src="test")
    assert "test.x" not in c.df.columns


def test_drop_empty():
    c = load_wide()
    c.drop()
    assert c.df.columns.tolist() == []
