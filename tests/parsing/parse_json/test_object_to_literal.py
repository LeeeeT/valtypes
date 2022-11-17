from typing import Literal

import pytest

import valtypes.error.parsing as error
import valtypes.error.parsing.literal as literal_error
from valtypes import parse_json


def test_returns_value_if_it_equals_to_one_of_literal_choices() -> None:
    assert parse_json(Literal[1], True) is True
    assert parse_json(Literal["1", "2", "3"], "2") == "2"


def test_parses_value_to_type_of_each_literal_choice() -> None:
    assert parse_json(Literal[1, False], 0) is False


def test_raises_error_if_value_doesnt_equal_to_any_literal_choices() -> None:
    with pytest.raises(literal_error.Composite) as info:
        parse_json(Literal["1", False], 1)

    assert info.value == literal_error.Composite(
        [literal_error.InvalidValue("1", error.WrongType(str, 1), 1), literal_error.NotMember(False, True)], 1
    )
