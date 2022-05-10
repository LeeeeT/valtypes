from valtypes.type.numeric import NegativeFloat


def test_non_negative_float() -> None:
    """
    It fails for a non-negative float
    """

    assert not NegativeFloat.check(1)
    assert not NegativeFloat.check(0)


def test_negative_float() -> None:
    """
    It succeeds for a negative float
    """

    assert NegativeFloat.check(-1)
