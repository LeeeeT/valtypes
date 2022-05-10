from valtypes.type.numeric import NegativeInt


def test_non_negative_int() -> None:
    """
    It fails for a non-negative int
    """

    assert not NegativeInt.check(1)
    assert not NegativeInt.check(0)


def test_negative_int() -> None:
    """
    It succeeds for a negative int
    """

    assert NegativeInt.check(-1)
