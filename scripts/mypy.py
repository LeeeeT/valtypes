import os

os.system("pip install poetry")
os.system("poetry install --with mypy")
os.system("mypy")
