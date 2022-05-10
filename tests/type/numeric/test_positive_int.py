from valtypes.type.numeric import PositiveInt


def test_non_positive_int() -> None:
    """
    It fails for a non-positive int
    """

    assert not PositiveInt.check(-1)
    assert not PositiveInt.check(0)


def test_positive_int() -> None:
    """
    It succeeds for a positive int
    """

    assert PositiveInt.check(1)
