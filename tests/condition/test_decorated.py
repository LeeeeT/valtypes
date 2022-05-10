from valtypes.condition import Equals, Wrap


def test() -> None:
    """
    It calls the decorator before passing a value to the condition
    """

    assert not (len >> Equals(2))("abc")
    assert (str.capitalize >> Wrap(str.isupper))("f")
