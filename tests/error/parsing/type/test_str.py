import re

from valtypes.error.parsing.type.str import Pattern


def test_pattern() -> None:
    assert str(Pattern(re.compile(r"^[a-z]+$"), "123")) == "the value doesn't match the pattern '^[a-z]+$', got: '123'"
