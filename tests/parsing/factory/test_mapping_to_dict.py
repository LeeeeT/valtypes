import testing.parsing.parser as testing_parser
from testing.parsing.factory import dummy
from valtypes.parsing import parser
from valtypes.parsing.factory import MappingToDict


def test_resolves_type_args() -> None:
    assert MappingToDict(dummy).get_parser_for(dict[int, str]) == parser.MappingToDict(testing_parser.Dummy(int), testing_parser.Dummy(str))
