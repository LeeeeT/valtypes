import pytest

import valtypes.error.parsing.type.sized as error
from valtypes import parse
from valtypes.type import str


def test_uses_constructor_to_parse_str_to_subclass_of_str() -> None:
    assert parse(str.NonEmpty, "abc") == "abc"

    with pytest.raises(error.MinimumLength):
        parse(str.NonEmpty, "")
