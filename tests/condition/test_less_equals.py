from valtypes.condition import LessEquals


def test_not_less_equals() -> None:
    """
    It returns False if a value is not less than or equal to another value
    """

    assert not LessEquals(1)(2)


def test_less_equals() -> None:
    """
    It returns True if a value is less than or equal to another value
    """

    assert LessEquals(1)(0)
    assert LessEquals(1)(1)
