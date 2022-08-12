import testing.parsing.parser as testing_parser
from testing.parsing.factory import dummy
from valtypes.parsing import parser
from valtypes.parsing.factory import ToUnion


def test_resolves_type_args() -> None:
    assert ToUnion(dummy).get_parser_for(int | float) == parser.ToUnion([testing_parser.Dummy(int), testing_parser.Dummy(float)])
