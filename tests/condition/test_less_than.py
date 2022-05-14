from valtypes.condition import LessThan


def test_not_less() -> None:
    """
    It returns False if the value isn't less than the exclusive maximum
    """

    assert not LessThan(1)(2)
    assert not LessThan(1)(1)


def test_less() -> None:
    """
    It returns True if the value is less than the exclusive maximum
    """

    assert LessThan(1)(0)
