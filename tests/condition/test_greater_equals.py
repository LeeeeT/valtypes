from valtypes.condition import GreaterEquals


def test_not_greater_equals() -> None:
    """
    It returns False if a value is not greater than or equal to another value
    """

    assert not GreaterEquals(1)(0)


def test_greater_equals() -> None:
    """
    It returns True if a value is greater than or equal to another value
    """

    assert GreaterEquals(1)(2)
    assert GreaterEquals(1)(1)
