from valtypes.condition import GreaterEquals


def test_not_greater_equals() -> None:
    """
    It returns False if the value isn't greater than or equal to the minimum
    """

    assert not GreaterEquals(1)(0)


def test_greater_equals() -> None:
    """
    It returns True if the value is greater than or equal to the minimum
    """

    assert GreaterEquals(1)(2)
    assert GreaterEquals(1)(1)
