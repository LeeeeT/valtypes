import valtypes.error.parsing.type.numeric as error


def test_maximum() -> None:
    e = error.Maximum(1, 2)
    assert str(e) == "the value must be less than or equal to 1, got: 2"


def test_minimum() -> None:
    e = error.Minimum(2, 1)
    assert str(e) == "the value must be greater than or equal to 2, got: 1"


def test_exclusive_maximum() -> None:
    e = error.ExclusiveMaximum(1, 1)
    assert str(e) == "the value must be less than 1, got: 1"


def test_exclusive_minimum() -> None:
    e = error.ExclusiveMinimum(2, 2)
    assert str(e) == "the value must be greater than 2, got: 2"
