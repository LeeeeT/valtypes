import re

import pytest

import valtypes.error.parsing.str as error
import valtypes.type.str as type


def test_raises_error_if_value_doesnt_match_pattern() -> None:
    class Str(type.RePattern):
        __pattern__ = re.compile("^[a-z]+$")

    with pytest.raises(error.RePatternNoMatch) as info:
        Str("123")

    assert info.value == error.RePatternNoMatch(re.compile("^[a-z]+$"), "123")


def test_succeeds_if_value_matches_pattern() -> None:
    class Str(type.RePattern):
        __pattern__ = re.compile("^[a-z]+$")

    Str("abc")
