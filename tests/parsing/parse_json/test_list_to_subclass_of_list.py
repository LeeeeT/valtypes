import pytest

import valtypes.error.parsing as error
import valtypes.error.parsing.type.sized as sized_error
from valtypes import parse_json
from valtypes.type import list


def test_parses_list_items() -> None:
    assert parse_json(list.NonEmpty[int], [False, 1, 2]) == [0, 1, 2]


def test_uses_constructor_to_parse_list_to_subclass_of_list() -> None:
    with pytest.raises(sized_error.MinimumLength):
        parse_json(list.NonEmpty[object], [])


def test_raises_error_if_cant_parse_some_item() -> None:
    with pytest.raises(error.Base):
        parse_json(list.NonEmpty[int], [0.0])
