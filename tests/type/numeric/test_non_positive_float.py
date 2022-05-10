from valtypes.type.numeric import NonPositiveFloat


def test_positive_float() -> None:
    """
    It fails for a positive float
    """

    assert not NonPositiveFloat.check(1)


def test_non_positive_float() -> None:
    """
    It succeeds for a non-positive float
    """

    assert NonPositiveFloat.check(-1)
    assert NonPositiveFloat.check(0)
