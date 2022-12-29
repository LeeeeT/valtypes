import pytest
import regex

import valtypes.error.parsing.str as error
import valtypes.type.str as type


def test_raises_error_if_value_doesnt_match_pattern() -> None:
    class Str(type.RegexPattern):
        __pattern__ = regex.compile("^[a-z]+$")

    with pytest.raises(error.RegexPatternNoMatch) as info:
        Str("123")

    assert info.value == error.RegexPatternNoMatch(regex.compile("^[a-z]+$"), "123")


def test_succeeds_if_value_matches_pattern() -> None:
    class Str(type.RegexPattern):
        __pattern__ = regex.compile("^[a-z]+$")

    Str("abc")
