from testing.error.parsing import Dummy
from valtypes.error.parsing import Union, WrongType


def test_wrong_type() -> None:
    assert str(WrongType("type", ...)) == "not an instance of 'type'"


def test_union_derive_returns_union_with_new_errors() -> None:
    assert Union([Dummy("cause")], 1).derive([Dummy("new cause")]) == Union([Dummy("new cause")], 1)
