from mltraq.utils.base_options import BaseOptions


class Options(BaseOptions):
    default_values = {
        "reproducibility": {"random_seed": 123},
        "tqdm": {"disable": False, "leave": False, "delay": 0},
        "transforms": {
            "src": "base",
            "dst": "base",
            "drop": True,
            "tmp": "temp",
        },
        "plot": {
            "save_to": None,
            "interactive": True,
        },
        "warnings": {"disable": True},
        "doc": {"url": "https://elehcimd.github.io/cumulative/"},
    }


def options() -> BaseOptions:
    """
    Returns singleton object of options.
    """

    return Options.instance()
