from valtypes.condition import LessEquals


def test_not_less_equals() -> None:
    """
    It returns False if the value isn't less than or equal to the maximum
    """

    assert not LessEquals(1)(2)


def test_less_equals() -> None:
    """
    It returns True if the value is less than or equal to the maximum
    """

    assert LessEquals(1)(0)
    assert LessEquals(1)(1)
