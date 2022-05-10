from valtypes.condition import GreaterThan


def test_not_greater() -> None:
    """
    It returns False if a value is not greater than another value
    """

    assert not GreaterThan(1)(0)
    assert not GreaterThan(1)(1)


def test_greater() -> None:
    """
    It returns True if a value is greater than another value
    """

    assert GreaterThan(1)(2)
