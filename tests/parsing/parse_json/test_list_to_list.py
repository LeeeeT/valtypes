import pytest

import valtypes.error.parsing as error
from valtypes import parse_json


def test_parses_list_items() -> None:
    assert parse_json(list[int], [False, 1, 2]) == [0, 1, 2]


def test_raises_error_if_cant_parse_some_item() -> None:
    with pytest.raises(error.Base):
        parse_json(list[int], [0.0])
