import valtypes.error.sized as error


def test_maximum_length() -> None:
    e = error.MaximumLength(1, 2)
    assert str(e) == "length 2 is greater than the allowed maximum of 1"


def test_minimum_length() -> None:
    e = error.MinimumLength(2, 1)
    assert str(e) == "length 1 is less than the allowed minimum of 2"
