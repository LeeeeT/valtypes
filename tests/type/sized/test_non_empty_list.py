from valtypes.type.sized import NonEmptyList


def test_empty() -> None:
    """
    It fails for an empty list
    """

    assert not NonEmptyList.check([])


def test_non_empty() -> None:
    """
    It succeeds for a non-empty list
    """

    assert NonEmptyList.check([...])
