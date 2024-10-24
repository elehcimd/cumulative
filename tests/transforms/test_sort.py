from cumulative.datasets.load_wide import load_wide


def test_sample():
    c = load_wide().sort(by="base.attr.rate")
    c.sample(n=1)
    assert len(c.df) == 1
