from typing import TypeVar

import pytest

from valtypes import BaseParsingError, parse

T = TypeVar("T")


def test_parse_items() -> None:
    """
    It parses list items to desired type
    """

    assert parse(set[int], [1, "2", b"3"]) == {1, 2, 3}


def test_wrong_item() -> None:
    """
    It throws an error if it can't parse some item to desired type
    """

    with pytest.raises(BaseParsingError):
        parse(set[int], [1, "2.5", b"3"])
