from cumulative.datasets.load_wide import load_wide


def test_sort():

    c = load_wide().sort(src="base.attr.rate")
    assert c.df["base.attr.rate"].iloc[0] == 2
