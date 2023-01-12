from valtypes.error.parsing.comparison import ExclusiveMaximum, ExclusiveMinimum, Maximum, Minimum


def test_maximum() -> None:
    assert str(Maximum(1, 2)) == "the value must be less than or equal to 1, got: 2"


def test_minimum() -> None:
    assert str(Minimum(2, 1)) == "the value must be greater than or equal to 2, got: 1"


def test_exclusive_maximum() -> None:
    assert str(ExclusiveMaximum(1, 1)) == "the value must be less than 1, got: 1"


def test_exclusive_minimum() -> None:
    assert str(ExclusiveMinimum(2, 2)) == "the value must be greater than 2, got: 2"
