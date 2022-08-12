import pytest

from valtypes import error, parse


def test_parses_list_items() -> None:
    assert parse(list[int], [False, 1, 2]) == [0, 1, 2]


def test_raises_if_cant_parse_some_item() -> None:
    with pytest.raises(error.Base):
        parse(list[int], [0.0])
