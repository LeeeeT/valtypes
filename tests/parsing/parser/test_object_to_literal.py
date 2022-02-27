from typing import Literal

import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import object_to_literal


def test_simple() -> None:
    assert object_to_literal.parse(Literal[1, "2"], "1.0", collection) == 1
    assert object_to_literal.parse(Literal[1, "2"], 2, collection) == "2"


def test_error() -> None:
    with pytest.raises(ParsingError):
        object_to_literal.parse(Literal[1, "2"], 2.0, collection)
