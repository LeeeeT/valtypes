import pytest

import valtypes.type.list as type


class List(type.LengthHook[int]):
    length: int | None

    def __length_hook__(self, length: int) -> None:
        self.length = length


class ErrorClass(type.LengthHook[object]):
    should_raise = False

    def __length_hook__(self, length: int) -> None:
        if self.should_raise:
            raise Exception


@pytest.fixture
def instance() -> List:
    instance = List(range(3))
    instance.length = None
    return instance


@pytest.fixture
def error_instance() -> ErrorClass:
    error_instance = ErrorClass(range(3))
    error_instance.should_raise = True
    return error_instance


def test_clear(instance: List) -> None:
    """
    It triggers the hook when `clear` is called
    """

    instance.clear()

    assert instance.length == 0
    assert instance == []


def test_clear_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.clear()

    assert error_instance == [0, 1, 2]


def test_append(instance: List) -> None:
    """
    It triggers the hook when `append` is called
    """

    instance.append(3)

    assert instance.length == 4
    assert instance == [0, 1, 2, 3]


def test_append_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.append(3)

    assert error_instance == [0, 1, 2]


def test_extend(instance: List) -> None:
    """
    It triggers the hook when `extend` is called
    """

    instance.extend(iter(range(3)))

    assert instance.length == 6
    assert instance == [0, 1, 2, 0, 1, 2]


def test_extend_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.extend(range(3))

    assert error_instance == [0, 1, 2]


def test_pop(instance: List) -> None:
    """
    It triggers the hook when `pop` is called
    """

    assert instance.pop() == 2
    assert instance.length == 2
    assert instance == [0, 1]


def test_pop_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.pop()

    assert error_instance == [0, 1, 2]


def test_insert(instance: List) -> None:
    """
    It triggers the hook when `insert` is called
    """

    instance.insert(0, -1)

    assert instance.length == 4
    assert instance == [-1, 0, 1, 2]


def test_insert_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.insert(0, -1)

    assert error_instance == [0, 1, 2]


def test_remove(instance: List) -> None:
    """
    It triggers the hook when `remove` is called
    """

    instance.remove(2)

    assert instance.length == 2
    assert instance == [0, 1]


def test_remove_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.remove(2)

    assert error_instance == [0, 1, 2]


def test_setitem_slice(instance: List) -> None:
    """
    It triggers the hook when `__setitem__` is called when passing a slice
    """

    instance[:-1] = iter((3,))

    assert instance.length == 2
    assert instance == [3, 2]


def test_setitem_not_slice(instance: List) -> None:
    """
    It doesn't trigger the hook when `__setitem__` is called with not a slice
    """

    instance[-1] = 0

    assert instance.length is None


def test_setitem_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance[:-1] = (3,)

    assert error_instance == [0, 1, 2]


def test_delitem_slice(instance: List) -> None:
    """
    It triggers the hook when `__delitem__` is called with a slice
    """

    del instance[:-1]

    assert instance.length == 1
    assert instance == [2]


def test_delitem_not_slice(instance: List) -> None:
    """
    It triggers the hook when `__delitem__` is called with not a slice
    """

    del instance[-1]

    assert instance.length == 2
    assert instance == [0, 1]


def test_delitem_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        del error_instance[-1]

    assert error_instance == [0, 1, 2]


def test_iadd(instance: List) -> None:
    """
    It triggers the hook when `__iadd__` is called
    """

    instance += iter(range(2))

    assert instance.length == 5
    assert instance == [0, 1, 2, 0, 1]


def test_iadd_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance += range(2)

    assert error_instance == [0, 1, 2]


def test_imul(instance: List) -> None:
    """
    It triggers the hook when `__imul__` is called
    """

    instance *= 3

    assert instance.length == 9
    assert instance == [0, 1, 2, 0, 1, 2, 0, 1, 2]


def test_imul_error(error_instance: ErrorClass) -> None:
    """
    It doesn't change the list if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance *= 3

    assert error_instance == [0, 1, 2]
