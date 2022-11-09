from testing.error.parsing.sequence import Dummy
from valtypes.error.parsing.sequence import Composite, WrongItem, WrongItemsCount


def test_composite_derive_returns_composite_with_new_errors() -> None:
    assert Composite([Dummy("cause")], 1).derive([Dummy("new cause")]) == Composite([Dummy("new cause")], 1)


def test_wrong_field_value_derive_returns_wrong_field_value_with_new_cause() -> None:
    assert WrongItem(1, Dummy("cause"), 1).derive([Dummy("new cause")]) == WrongItem(1, Dummy("new cause"), 1)


def test_wrong_item() -> None:
    assert WrongItem(42, Dummy("cause"), ...).message == "can't parse item at index 42"


def test_wrong_items_count() -> None:
    assert str(WrongItemsCount(1, 2)) == "1 item(s) expected, got 2"
