import re

import pytest

import valtypes.error.parsing.str as error
from valtypes import parse_json


def test_compiles_str_to_pattern() -> None:
    assert parse_json(re.Pattern[str], "abc") == re.compile("abc")


def test_raises_error_if_cant_compile_pattern() -> None:
    with pytest.raises(error.RePatternCompilation) as info:
        parse_json(re.Pattern[str], "(")

    assert info.value == error.RePatternCompilation("(")
