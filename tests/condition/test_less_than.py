from valtypes.condition import LessThan


def test_not_less() -> None:
    """
    It returns False if a value is not less than another value
    """

    assert not LessThan(1)(2)
    assert not LessThan(1)(1)


def test_less() -> None:
    """
    It returns True if a value is less than another value
    """

    assert LessThan(1)(0)
