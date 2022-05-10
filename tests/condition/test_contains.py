from valtypes.condition import Contains


def test_not_contains() -> None:
    """
    It returns False if a value does not contain the desired value
    """

    assert not Contains(1)([])


def test_contains() -> None:
    """
    It returns True if a value contains the desired value
    """

    assert Contains(1)([1, 2, 3])
