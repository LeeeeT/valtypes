from valtypes.condition import Equals


def test_not_equal() -> None:
    """
    It returns False if values are not equal
    """

    assert not Equals(1)("1")


def test_equal() -> None:
    """
    It returns True if values are equal
    """

    assert Equals(1.0)(1)
