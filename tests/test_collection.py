from valtypes import Collection


def test_empty_creates_empty_collection() -> None:
    assert list(Collection[object].empty()) == []


def test_iter_iterates_through_items() -> None:
    assert list(Collection([1, 2, 3])) == [1, 2, 3]


def test_add_to_top_adds_objects_to_top() -> None:
    collection = Collection[int].empty()
    collection.add_to_top(1)

    assert list(collection) == [1]

    collection.add_to_top(2, 3)

    assert list(collection) == [2, 3, 1]


def test_add_to_end_adds_objects_to_end() -> None:
    collection = Collection[int].empty()
    collection.add_to_end(1)

    assert list(collection) == [1]

    collection.add_to_end(2, 3)

    assert list(collection) == [1, 2, 3]
