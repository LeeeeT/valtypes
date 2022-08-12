import pytest

import valtypes.type.set as type


class Set(type.LengthHook[int]):
    length: int | None

    def __length_hook__(self, length: int) -> None:
        self.length = length


class ErrorSet(type.LengthHook[object]):
    should_raise = False

    def __length_hook__(self, length: int) -> None:
        if self.should_raise:
            raise Exception


@pytest.fixture
def instance() -> Set:
    instance = Set(range(3))
    instance.length = None
    return instance


@pytest.fixture
def error_instance() -> ErrorSet:
    error_instance = ErrorSet(range(3))
    error_instance.should_raise = True
    return error_instance


def test_add(instance: Set) -> None:
    """
    It triggers the hook when `add` is called if an element isn't present in the set
    """

    instance.add(3)

    assert instance.length == 4
    assert instance == {0, 1, 2, 3}


def test_add_present(instance: Set) -> None:
    """
    It doesn't trigger the hook when `add` is called if an element is present in the set
    """

    instance.add(1)

    assert instance.length is None


def test_add_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.add(3)

    assert error_instance == {0, 1, 2}


def test_difference_update(instance: Set) -> None:
    """
    It triggers the hook when `difference_update` is called
    """

    instance.difference_update(iter((0,)), iter((2,)))

    assert instance.length == 1
    assert instance == {1}


def test_difference_update_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.difference_update((0,), (2,))

    assert error_instance == {0, 1, 2}


def test_discard(instance: Set) -> None:
    """
    It triggers the hook when `discard` is called if an element is present in the set
    """

    instance.discard(1)

    assert instance.length == 2
    assert instance == {0, 2}


def test_discard_present(instance: Set) -> None:
    """
    It doesn't trigger the hook when `discard` is called if an element isn't present in the set
    """

    instance.discard(3)

    assert instance.length is None


def test_discard_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.discard(1)

    assert error_instance == {0, 1, 2}


def test_intersection_update(instance: Set) -> None:
    """
    It triggers the hook when `intersection_update` is called
    """

    instance.intersection_update(iter((0, 1)), iter((1, 2)))

    assert instance.length == 1
    assert instance == {1}


def test_intersection_update_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.intersection_update((0, 1), (1, 2))

    assert error_instance == {0, 1, 2}


def test_clear(instance: Set) -> None:
    """
    It triggers the hook when `clear` is called
    """

    instance.clear()

    assert instance.length == 0
    assert instance == set()


def test_clear_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.clear()

    assert error_instance == {0, 1, 2}


def test_pop(instance: Set) -> None:
    """
    It triggers the hook when `pop` is called
    """

    assert instance.pop() == 0
    assert instance.length == 2
    assert instance == {1, 2}


def test_pop_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.pop()

    assert error_instance == {0, 1, 2}


def test_remove(instance: Set) -> None:
    """
    It triggers the hook when `remove` is called
    """

    instance.remove(1)

    assert instance.length == 2
    assert instance == {0, 2}


def test_remove_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.remove(1)

    assert error_instance == {0, 1, 2}


def test_symmetric_difference_update(instance: Set) -> None:
    """
    It triggers the hook when `symmetric_difference_update` is called with a slice
    """

    instance.symmetric_difference_update(iter(range(1, 4)))

    assert instance.length == 2
    assert instance == {0, 3}


def test_symmetric_difference_update_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.symmetric_difference_update(range(1, 4))

    assert error_instance == {0, 1, 2}


def test_update(instance: Set) -> None:
    """
    It triggers the hook when `update` is called
    """

    instance.update(iter((2, 3)), iter((3, 4)))

    assert instance.length == 5
    assert instance == {0, 1, 2, 3, 4}


def test_update_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance.update((2, 3), (3, 4))

    assert error_instance == {0, 1, 2}


def test_iand(instance: Set) -> None:
    """
    It triggers the hook when `__iand__` is called
    """

    instance &= {0, 1}

    assert instance.length == 2
    assert instance == {0, 1}


def test_iand_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance &= {0, 1}

    assert error_instance == {0, 1, 2}


def test_ior(instance: Set) -> None:
    """
    It triggers the hook when `__ior__` is called
    """

    instance |= {2, 3}

    assert instance.length == 4
    assert instance == {0, 1, 2, 3}


def test_ior_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance |= {2, 3}

    assert error_instance == {0, 1, 2}


def test_isub(instance: Set) -> None:
    """
    It triggers the hook when `__isub__` is called
    """

    instance -= {0}

    assert instance.length == 2
    assert instance == {1, 2}


def test_isub_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance -= {0}

    assert error_instance == {0, 1, 2}


def test_ixor(instance: Set) -> None:
    """
    It triggers the hook when `__ixor__` is called with a slice
    """

    instance ^= {1, 2, 3}

    assert instance.length == 2
    assert instance == {0, 3}


def test_ixor_error(error_instance: ErrorSet) -> None:
    """
    It doesn't change the set if the hook raises an error
    """

    with pytest.raises(Exception):
        error_instance ^= {1, 2, 3}

    assert error_instance == {0, 1, 2}
