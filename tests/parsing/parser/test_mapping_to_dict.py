from testing.parsing.parser import Const
from valtypes.parsing.parser import MappingToDict


def test_eq_returns_true_if_parsers_are_equal() -> None:
    assert MappingToDict(Const(1), Const(2)) == MappingToDict(Const(1), Const(2))


def test_eq_returns_false_if_parsers_are_different() -> None:
    assert MappingToDict(Const(1), Const(2)) != MappingToDict(Const(1), Const(1))
    assert MappingToDict(Const(1), Const(2)) != MappingToDict(Const(2), Const(2))


def test_eq_returns_not_implemented_if_got_not_mapping_to_union() -> None:
    assert MappingToDict(Const(1), Const(2)) != ...
