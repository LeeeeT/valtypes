from valtypes.error.parsing.sized import MaximumLength, MinimumLength


def test_maximum_length() -> None:
    assert str(MaximumLength(1, 2)) == "length 2 is greater than the allowed maximum of 1"


def test_minimum_length() -> None:
    assert str(MinimumLength(2, 1)) == "length 1 is less than the allowed minimum of 2"
