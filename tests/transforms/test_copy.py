from cumulative.datasets.load_wide import load_wide


def test_copy():
    """
    Test: We can copy columns by prefix.
    """

    c = load_wide()
    c.copy(dst="test")

    # Test presence of a destination column.
    assert "test.x" in c.df.columns
