from valtypes.condition import Contains


def test_not_contains() -> None:
    """
    It returns False if the value doesn't contain the desired value
    """

    assert not Contains(1)([])


def test_contains() -> None:
    """
    It returns True if the value contains the desired value
    """

    assert Contains(1)([1, 2, 3])
