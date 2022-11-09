import os

os.system("pip install poetry")
os.system("poetry install --with pyright")
os.system("pyright")
