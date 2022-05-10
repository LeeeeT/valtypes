from valtypes.type.sized import NonEmptyTuple


def test_empty() -> None:
    """
    It fails for an empty list
    """

    assert not NonEmptyTuple.check(())


def test_non_empty() -> None:
    """
    It succeeds for a non-empty list
    """

    assert NonEmptyTuple.check((...,))
