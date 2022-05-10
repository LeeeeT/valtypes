from valtypes.type.sized import NonEmptyFrozenset


def test_empty() -> None:
    """
    It fails for an empty frozenset
    """

    assert not NonEmptyFrozenset.check(frozenset())


def test_non_empty() -> None:
    """
    It succeeds for a non-empty frozenset
    """

    assert NonEmptyFrozenset.check(frozenset({...}))
