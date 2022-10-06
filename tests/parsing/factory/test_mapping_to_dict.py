import testing.parsing.parser as test_parser
from testing.parsing.factory import dummy
from valtypes.parsing import parser
from valtypes.parsing.factory import MappingToDict


def test_resolves_type_args() -> None:
    assert MappingToDict(dummy).get_parser_for(dict[int, str]) == parser.MappingToDict(test_parser.Dummy(int), test_parser.Dummy(str))
