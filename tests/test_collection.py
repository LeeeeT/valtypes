from valtypes import Collection


def test_empty() -> None:
    """
    It creates an empty collection
    """

    assert list(Collection[object].empty()) == []


def test_iter() -> None:
    """
    It iterates through the collection items
    """

    assert list(Collection([1, 2, 3])) == [1, 2, 3]


def test_add_to_top() -> None:
    """
    It adds objects to the top of the collection
    """

    collection = Collection[int].empty()
    collection.add_to_top(1)

    assert list(collection) == [1]

    collection.add_to_top(2, 3)

    assert list(collection) == [2, 3, 1]


def test_add_to_end() -> None:
    """
    It adds objects to the end of the collection
    """

    collection = Collection[int].empty()
    collection.add_to_end(1)

    assert list(collection) == [1]

    collection.add_to_end(2, 3)

    assert list(collection) == [1, 2, 3]
