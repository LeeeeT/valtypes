from testing.error.parsing.dataclass import Dummy
from valtypes.error.parsing.dataclass import Composite, MissingField, WrongFieldValue


def test_wrong_field_value() -> None:
    assert WrongFieldValue("field", Dummy("cause"), ...).message == "can't parse field 'field'"


def test_composite_derive_returns_composite_with_new_errors() -> None:
    assert Composite([Dummy("cause")], {}).derive([Dummy("new cause")]) == Composite([Dummy("new cause")], {})


def test_wrong_field_value_derive_returns_wrong_field_value_with_new_cause() -> None:
    assert WrongFieldValue("field", Dummy("cause"), 1).derive([Dummy("new cause")]) == WrongFieldValue("field", Dummy("new cause"), 1)


def test_missing_field() -> None:
    assert str(MissingField("field")) == "required field 'field' is missing"
