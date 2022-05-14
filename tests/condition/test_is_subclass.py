from valtypes.condition import IsSubclass


def test_not_class() -> None:
    """
    It returns False if the value isn't a class
    """

    assert not IsSubclass(float)(3.14)


def test_not_subclass() -> None:
    """
    It returns False if the value isn't a subclass of the desired class
    """

    assert not IsSubclass(float)(int)


def test_subclass() -> None:
    """
    It returns True if the value is a subclass of the desired class or is the desired class itself
    """

    assert IsSubclass(int)(int)
    assert IsSubclass(int)(bool)
