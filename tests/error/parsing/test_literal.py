from testing.error.parsing.literal import Dummy
from valtypes.error.parsing.literal import Composite, InvalidValue, NotMember


def test_composite_derive_returns_composite_with_new_errors() -> None:
    assert Composite([Dummy("cause")], 1).derive([Dummy("new cause")]) == Composite([Dummy("new cause")], 1)


def test_invalid_value_derive_returns_invalid_value_with_new_cause() -> None:
    assert InvalidValue(1, Dummy("cause"), 2).derive([Dummy("new cause")]) == InvalidValue(1, Dummy("new cause"), 2)


def test_not_member() -> None:
    assert str(NotMember(1, 2)) == "the value is not 1"
