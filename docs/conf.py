import pathlib
import re

current_dir = pathlib.Path(__file__).resolve().parent.parent

pyproject_file = (current_dir / "pyproject.toml").read_text()
license_file = (current_dir / "LICENSE").read_text()

project = re.search(r"name = \"(.*)\"", pyproject_file).groups()[0]
copyright = re.search(r"Copyright \(c\) (.*)", license_file).groups()[0]
author = re.search(r"authors = \[\"([^\"]*) <.*", pyproject_file).groups()[0]
release = version = re.search(r"version = \"(.*)\"", pyproject_file).groups()[0]

extensions = []

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]
