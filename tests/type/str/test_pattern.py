import re

import pytest

import valtypes.error.str as error
import valtypes.type.str as type


def test_raises_error_if_str_does_not_match_pattern() -> None:
    class Str(type.Pattern):
        __pattern__ = re.compile("^[a-z]+$")

    with pytest.raises(error.Pattern) as info:
        Str("123")

    assert info.value == error.Pattern(re.compile("^[a-z]+$"), "123")


def test_succeeds_if_str_matches_pattern() -> None:
    class Str(type.Pattern):
        __pattern__ = re.compile("^[a-z]+$")

    Str("abc")
