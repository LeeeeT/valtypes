from subprocess import call

exit(call(["pip", "install", "poetry"]) or call(["poetry", "install", "--with", "pyright-verify"]) or call(["pyright", "--verifytypes", "valtypes"]))
