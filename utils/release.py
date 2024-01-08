import os

from common import execute, get_package_version, project_dir, project_name


def inc_version():
    execute("poetry version patch")

    pkg_version = get_package_version(f"{project_dir}/pyproject.toml")

    with open(f"{project_dir}/src/{project_name}/version.py", "w") as f:
        f.write(f'__version__ = "{pkg_version}"\n')

    return pkg_version


def pytest():
    execute("poetry run pytest")


def main():
    os.chdir(project_dir)

    execute("python utils/build_package.py")
    execute("python utils/build_docs.py")
    execute("mkdocs gh-deploy")

    print("\n\n--")
    print("Documentation available at: https://elehcimd.github.io/cumulative/")
    print('To publish:\n 1. $ poetry "-u$PYPI_USERNAME" "-p$PYPI_PASSWORD" --build publish\n 2. update repository')


if __name__ == "__main__":
    main()
