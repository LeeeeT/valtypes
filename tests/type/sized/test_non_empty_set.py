from valtypes.type.sized import NonEmptySet


def test_empty() -> None:
    """
    It fails for an empty set
    """

    assert not NonEmptySet.check(set())


def test_non_empty() -> None:
    """
    It succeeds for a non-empty set
    """

    assert NonEmptySet.check({...})
