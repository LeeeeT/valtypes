from subprocess import call

exit(call(["pip", "install", "poetry"]) or call(["poetry", "install", "--with", "pyright"]) or call(["pyright"]))
