from valtypes.condition import Wrap


def test() -> None:
    """
    It wraps the condition
    """

    assert Wrap(str.istitle).condition is str.istitle
    assert not Wrap(str.istitle)("f")
