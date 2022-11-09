from subprocess import call

exit(call(["pip", "install", "poetry"]) or call(["poetry", "install", "--with", "mypy"]) or call(["mypy"]))
