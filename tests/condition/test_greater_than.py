from valtypes.condition import GreaterThan


def test_not_greater() -> None:
    """
    It returns False if the value isn't greater than the exclusive minimum
    """

    assert not GreaterThan(1)(0)
    assert not GreaterThan(1)(1)


def test_greater() -> None:
    """
    It returns True if the value is greater than the exclusive minimum
    """

    assert GreaterThan(1)(2)
