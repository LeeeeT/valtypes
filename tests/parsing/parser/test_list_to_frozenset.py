from typing import TypeVar

import pytest

from valtypes import BaseParsingError, parse

T = TypeVar("T")


def test_parse_values() -> None:
    """
    It parses the list items to the desired type
    """

    assert parse(frozenset[int], [1, "2", b"3"]) == {1, 2, 3}


def test_wrong_item() -> None:
    """
    It raises an error if it can't parse some item to the desired type
    """

    with pytest.raises(BaseParsingError):
        parse(frozenset[int], [1, "2.5", b"3"])
