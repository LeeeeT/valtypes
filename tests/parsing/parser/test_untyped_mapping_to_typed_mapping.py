from collections.abc import Mapping

import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import untyped_mapping_to_typed_mapping


def test_simple() -> None:
    assert untyped_mapping_to_typed_mapping.parse(Mapping[str, int], {False: "0.0", 1: "1"}, collection) == {
        "False": 0,
        "1": 1,
    }


def test_error() -> None:
    with pytest.raises(ParsingError):
        untyped_mapping_to_typed_mapping.parse(Mapping[int, int], {1: 1.5}, collection)
