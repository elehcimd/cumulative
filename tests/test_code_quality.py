import os
import subprocess

from flake8.api import legacy as flake8


def local(args):
    cmd = " ".join(args) if isinstance(args, list) else args
    return subprocess.check_output(cmd, shell=True).decode("utf-8")  # noqa


def test_vulture():
    assert local("vulture src utils vulture_whitelist.py") == ""


def test_ruff():
    # Run once to auto-fix errors
    local("ruff . --fix --exit-zero")

    # Test again
    assert local("ruff . --exit-zero") == ""


def test_black():
    local("black .")


def test_pep8():
    # By default, flake8 will pick up the configuration file from the project directory.
    files = [os.path.dirname(os.path.abspath(__file__)) + "/../src"]
    files += [os.path.dirname(os.path.abspath(__file__)) + "/../tests"]
    files += [os.path.dirname(os.path.abspath(__file__)) + "/../utils"]
    report = flake8.get_style_guide(quiet=False).check_files(files)

    # Get all violations
    violations = report.get_statistics("")

    # If not empty, test is failed.
    if violations != []:
        raise Exception(f"Flake8 found violations: {violations}")
