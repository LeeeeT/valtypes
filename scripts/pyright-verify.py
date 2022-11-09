import os

os.system("pip install poetry")
os.system("poetry install --with pyright-verify")
os.system("pyright --verifytypes valtypes")
