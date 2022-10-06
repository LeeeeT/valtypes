import re

import valtypes.error.str as error


def test_pattern() -> None:
    e = error.Pattern(re.compile("^[a-z]+$"), "123")
    assert str(e) == "the value doesn't match the pattern '^[a-z]+$', got: '123'"
