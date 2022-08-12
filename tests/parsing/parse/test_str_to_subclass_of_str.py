import pytest

import valtypes.error.sized as sized_error
from valtypes import parse
from valtypes.type import str


def test_uses_constructor_to_parse_float_to_subclass_of_float() -> None:
    assert parse(str.NonEmpty, "abc") == "abc"

    with pytest.raises(sized_error.MinimumLength):
        parse(str.NonEmpty, "")
