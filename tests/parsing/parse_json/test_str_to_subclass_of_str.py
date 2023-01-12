import pytest

import valtypes.error.parsing.sized as error
from valtypes import parse_json
from valtypes.type import str


def test_uses_constructor_to_parse_str_to_subclass_of_str() -> None:
    assert parse_json(str.NonEmpty, "abc") == "abc"

    with pytest.raises(error.MinimumLength):
        parse_json(str.NonEmpty, "")
