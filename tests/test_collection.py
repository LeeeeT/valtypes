from valtypes import Collection


def test_iter() -> None:
    """
    It iterates through the collection items
    """

    assert list(Collection([1, 2, 3])) == [1, 2, 3]


def test_add() -> None:
    """
    It adds an item to the collection
    """

    collection = Collection[int]()
    collection.add(1)

    assert list(collection) == [1]

    collection.add(2, 3)

    assert list(collection) == [1, 2, 3]
