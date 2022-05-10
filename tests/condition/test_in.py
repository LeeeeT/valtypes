from valtypes.condition import In


def test_not_member() -> None:
    """
    It returns False if a value is not a member of the container
    """

    assert not In([2])(1)


def test_member() -> None:
    """
    It returns True if a value is a member of the container
    """

    assert In([1, 2, 3])(1)
