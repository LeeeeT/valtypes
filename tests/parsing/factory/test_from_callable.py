from typing import Any

from valtypes.parsing import parser
from valtypes.parsing.factory import FromCallable


def test_calls_callable() -> None:
    assert FromCallable[type, object, Any](parser.ObjectToType).get_parser_for(str) == parser.ObjectToType(str)
