import glob
import io
import os
import subprocess
import sys
import warnings
from contextlib import redirect_stdout
from typing import List

from cumulative.opts import options

project_dir = os.path.abspath(os.path.dirname(__file__) + os.sep + os.pardir)
project_name = os.path.basename(project_dir)


def local(args) -> str:
    cmd = " ".join(args) if isinstance(args, list) else args
    return subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True).decode("utf-8")  # noqa


def local_python(pathname: str) -> str:
    # Execute Python code contained in file
    with open(pathname) as f:
        data = f.readlines()
        func_code = "\n".join([f"\t{line}" for line in data])
        data_f = f"def local_python_func():\n{func_code}\nlocal_python_func()"

    f = io.StringIO()
    with options().ctx({"plot.ctx.default.interactive_mode": False, "plot.ctx.default.savefig_svg": f"{pathname}.svg"}):
        with redirect_stdout(f):
            exec(data_f)  # noqa
    return f.getvalue()


def check_usage(py_files: List[str]):
    md_files = glob.glob("mkdocs/**/*.md", recursive=True)
    md_text = "".join([open(md_file).read() for md_file in md_files])
    for py_file in py_files:
        if py_file not in md_text:
            warnings.warn(f"Warning: {py_file} not linked", stacklevel=1)


def main(argv):
    os.chdir(project_dir)

    if len(argv) > 1:
        pattern = argv[1]
        print(f"Limiting to files matching pattern '{pattern}'")
    else:
        pattern = ""

    rm_files = glob.glob(f"mkdocs/**/*{pattern}*.out", recursive=True) + glob.glob(
        f"mkdocs/**/*{pattern}*.src", recursive=True
    )
    # Make sure we don't remove images in the assets directory that are not regenerated.
    rm_assets = glob.glob(f"mkdocs/**/*{pattern}*.svg", recursive=True)
    rm_assets = [f for f in rm_assets if "/img/examples/" in f]
    rm_files += rm_assets

    print("Removing outputs")
    for idx, rm_file in enumerate(rm_files):
        print(f"[{idx+1}/{len(rm_files)}] Removing {rm_file}")
        os.remove(rm_file)

    py_files = glob.glob(f"mkdocs/**/*{pattern}*.py", recursive=True)
    py_files = [py_file for py_file in py_files if py_file != "mkdocs/mymacros.py"]

    check_usage(py_files)

    print("Executing examples ...")
    for idx, py_file in enumerate(py_files):
        print(f"[{idx+1}/{len(py_files)}] Executing {py_file}")
        out = local_python(py_file)
        with open(f"{py_file}.out", "w") as f:
            f.write(out)

        out = local(f'sh -c "cat {py_file} | black --line-length 75 -q -"')
        with open(f"{py_file}.src", "w") as f:
            f.write(out)

    local("touch mkdocs.yml")

    print("Operation completed.")


if __name__ == "__main__":
    main(sys.argv)
