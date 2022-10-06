import valtypes.error.float as error


def test_exclusive_maximum() -> None:
    e = error.ExclusiveMaximum(1, 1)
    assert str(e) == "the value must be less than 1, got: 1"


def test_exclusive_minimum() -> None:
    e = error.ExclusiveMinimum(2, 2)
    assert str(e) == "the value must be greater than 2, got: 2"
