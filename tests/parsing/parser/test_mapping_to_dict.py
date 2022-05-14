from typing import TypeVar

import pytest

from valtypes import BaseParsingError, parse

T = TypeVar("T")
F = TypeVar("F")


def test_parse_keys_and_values() -> None:
    """
    It parses the keys and values of the mapping to the desired types
    """

    assert parse(dict[str, int], {False: "0.0", 1: "1"}) == {"False": 0, "1": 1}


def test_wrong_key_or_value() -> None:
    """
    It raises an error if it can't parse some key or value to the desired type
    """

    with pytest.raises(BaseParsingError):
        parse(dict[int, int], {1: 1.5})
