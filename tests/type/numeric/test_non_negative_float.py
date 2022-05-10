from valtypes.type.numeric import NonNegativeFloat


def test_negative_float() -> None:
    """
    It fails for a negative float
    """

    assert not NonNegativeFloat.check(-1)


def test_non_negative_float() -> None:
    """
    It succeeds for a non-negative float
    """

    assert NonNegativeFloat.check(1)
    assert NonNegativeFloat.check(0)
