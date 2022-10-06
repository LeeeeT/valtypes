from testing.parsing import parser
from valtypes.parsing.factory import FromCallable

__all__ = ["dummy"]


@FromCallable
def dummy(type: object, /) -> parser.Dummy:
    return parser.Dummy(type)
