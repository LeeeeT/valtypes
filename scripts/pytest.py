import os

os.system("pip install poetry")
os.system("poetry install --with pytest")
os.system("pytest")
