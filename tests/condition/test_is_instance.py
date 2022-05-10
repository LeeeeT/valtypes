from valtypes.condition import IsInstance


def test_not_instance() -> None:
    """
    It returns False if a value is not an instance of the type
    """

    assert not IsInstance(int)("1")
    assert not IsInstance(list[int])([1])


def test_instance() -> None:
    """
    It returns True if a value is an instance of the type
    """

    assert IsInstance(int | float)(1.0)
