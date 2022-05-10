from valtypes.type.numeric import NonPositiveInt


def test_positive_int() -> None:
    """
    It fails for a positive int
    """

    assert not NonPositiveInt.check(1)


def test_non_positive_int() -> None:
    """
    It succeeds for a non-positive int
    """

    assert NonPositiveInt.check(-1)
    assert NonPositiveInt.check(0)
