import pytest
import regex

import valtypes.error.parsing.str as error
from valtypes import parse_json


def test_compiles_str_to_pattern() -> None:
    assert parse_json(regex.Pattern[str], "abc") == regex.compile("abc")


def test_raises_error_if_cant_compile_pattern() -> None:
    with pytest.raises(error.RegexPatternCompilation) as info:
        parse_json(regex.Pattern[str], "(")

    assert info.value == error.RegexPatternCompilation("(")
