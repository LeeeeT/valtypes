from typing import Literal

import pytest

from valtypes import BaseParsingError, parse


def test_parse_to_choice_type() -> None:
    """
    It parses a value to the type of Literal choice before equality checking
    """

    assert parse(Literal[1, "2"], "1.0") == 1
    assert parse(Literal[1, "2"], 2) == "2"


def test_wrong_value() -> None:
    """
    It throws an error if a value does not match any Literal choices
    """

    with pytest.raises(BaseParsingError):
        parse(Literal[1, "2"], 2.0)
