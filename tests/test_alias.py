from valtypes.alias import ALIASES_KEY, Alias


def test() -> None:
    """
    It creates a dict containing aliases
    """

    assert Alias("a", "b") == {ALIASES_KEY: ("a", "b")}
