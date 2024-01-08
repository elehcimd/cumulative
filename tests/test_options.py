from cumulative.options import options


def test_option_get():
    # Test the value of a default value
    assert options.get("reproducibility.random_seed") == 123


def test_option_set_reset():
    # Test the change of a default value
    options.set("reproducibility.random_seed", 124)
    assert options.get("reproducibility.random_seed") == 124

    # Test the reset to default values
    options.reset("reproducibility.random_seed")
    assert options.get("reproducibility.random_seed") == 123


def test_option_get_default():
    # Test the returned value if NOT null
    v = options.default_if_null(200, "reproducibility.random_seed")
    assert v == 200

    # Test the returned value if null
    v = options.default_if_null(None, "reproducibility.random_seed")
    assert v == 123


def test_option_context():
    # Test the context custom values for options
    assert options.get("reproducibility.random_seed") == 123
    with options.option_context({"reproducibility.random_seed": 124}):
        assert options.get("reproducibility.random_seed") == 124
    assert options.get("reproducibility.random_seed") == 123
