# brew install svgo

import glob
import os
import shutil
import sys

from common import local, project_dir


def main(argv):
    os.chdir(project_dir)

    matches = glob.glob("mkdocs/**/demo/*.svg", recursive=True)
    for match in matches:
        print(f"Optimizing and removing background color in {match} ..")
        print(local(f"svgo {match} -o tmp.svg"))
        shutil.move("tmp.svg", match)
        data = open(match).read()
        data = data.replace("fill:#fff", "fill:none")
        with open(match, "w") as f:
            f.write(data)


if __name__ == "__main__":
    main(sys.argv)
