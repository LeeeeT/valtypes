from valtypes.type.numeric import NonNegativeInt


def test_negative_int() -> None:
    """
    It fails for a negative int
    """

    assert not NonNegativeInt.check(-1)


def test_non_negative_int() -> None:
    """
    It succeeds for a non-negative int
    """

    assert NonNegativeInt.check(1)
    assert NonNegativeInt.check(0)
