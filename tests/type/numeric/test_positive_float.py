from valtypes.type.numeric import PositiveFloat


def test_non_positive_float() -> None:
    """
    It fails for a non-positive float
    """

    assert not PositiveFloat.check(-1)
    assert not PositiveFloat.check(0)


def test_positive_float() -> None:
    """
    It succeeds for a positive float
    """

    assert PositiveFloat.check(1)
