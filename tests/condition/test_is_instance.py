from valtypes.condition import IsInstance


def test_not_instance() -> None:
    """
    It returns False if the value isn't an instance of the desired type
    """

    assert not IsInstance(int)("1")
    assert not IsInstance(list[int])([1])


def test_instance() -> None:
    """
    It returns True if the value is an instance of the desired type
    """

    assert IsInstance(int | float)(1.0)
