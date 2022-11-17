from testing.parsing import factory as testing_factory
from testing.parsing import parser as testing_parser
from valtypes.parsing import parser
from valtypes.parsing.factory import ToSubclassOf


def test() -> None:
    assert ToSubclassOf[float, object](float, testing_factory.dummy).get_parser_for(int) == testing_parser.Dummy(float) >> parser.FromCallable(int)
