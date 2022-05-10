from valtypes.type.numeric import Portion


def test_less_than_0() -> None:
    """
    It fails for numbers less than 0
    """

    assert not Portion.check(-0.1)


def test_greater_than_1() -> None:
    """
    It fails for numbers greater than 1
    """

    assert not Portion.check(1.1)


def test_from_0_to_1() -> None:
    """
    It succeeds for numbers in the range [0, 1]
    """

    assert Portion.check(0)
    assert Portion.check(0.5)
    assert Portion.check(1)
