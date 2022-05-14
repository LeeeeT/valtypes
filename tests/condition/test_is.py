from valtypes.condition import Is


def test_not_identical() -> None:
    """
    It returns False if the values aren't identical
    """

    assert not Is(False)(True)


def test_identical() -> None:
    """
    It returns True if the values are identical
    """

    assert Is(True)(True)
