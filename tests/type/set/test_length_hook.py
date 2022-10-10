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


def test_triggers_hook_when_add_is_called_and_element_is_not_present(instance: Set) -> None:
    instance.add(3)

    assert instance.length == 4
    assert instance == {0, 1, 2, 3}


def test_doesnt_trigger_hook_when_add_is_called_and_element_is_present(instance: Set) -> None:
    instance.add(1)

    assert instance.length is None


def test_doesnt_change_value_if_hook_raised_error_when_add_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.add(3)

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_difference_update_is_called(instance: Set) -> None:
    instance.difference_update(iter((0,)), iter((2,)))

    assert instance.length == 1
    assert instance == {1}


def test_doesnt_change_value_if_hook_raised_error_when_difference_update_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.difference_update((0,), (2,))

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_discard_is_called_and_element_is_present(instance: Set) -> None:
    instance.discard(1)

    assert instance.length == 2
    assert instance == {0, 2}


def test_doesnt_trigger_hook_when_discard_is_called_and_element_is_not_present(instance: Set) -> None:
    instance.discard(3)

    assert instance.length is None


def test_doesnt_change_value_if_hook_raised_error_when_discard_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.discard(1)

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_intersection_update_is_called(instance: Set) -> None:
    instance.intersection_update(iter((0, 1)), iter((1, 2)))

    assert instance.length == 1
    assert instance == {1}


def test_doesnt_change_value_if_hook_raised_error_when_intersection_update_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.intersection_update((0, 1), (1, 2))

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_clear_is_called(instance: Set) -> None:
    instance.clear()

    assert instance.length == 0
    assert instance == set()


def test_doesnt_change_value_if_hook_raised_error_when_clear_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.clear()

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_pop_is_called(instance: Set) -> None:
    assert instance.pop() == 0
    assert instance.length == 2
    assert instance == {1, 2}


def test_doesnt_change_value_if_hook_raised_error_when_pop_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.pop()

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_remove_is_called(instance: Set) -> None:
    instance.remove(1)

    assert instance.length == 2
    assert instance == {0, 2}


def test_doesnt_change_value_if_hook_raised_error_when_remove_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.remove(1)

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_symmetric_difference_update_is_called(instance: Set) -> None:
    instance.symmetric_difference_update(iter(range(1, 4)))

    assert instance.length == 2
    assert instance == {0, 3}


def test_doesnt_change_value_if_hook_raised_error_when_symmetric_difference_update_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.symmetric_difference_update(range(1, 4))

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_update_is_called(instance: Set) -> None:
    instance.update(iter((2, 3)), iter((3, 4)))

    assert instance.length == 5
    assert instance == {0, 1, 2, 3, 4}


def test_doesnt_change_value_if_hook_raised_error_when_update_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance.update((2, 3), (3, 4))

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_iand_is_called(instance: Set) -> None:
    instance &= {0, 1}

    assert instance.length == 2
    assert instance == {0, 1}


def test_doesnt_change_value_if_hook_raised_error_when_iand_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance &= {0, 1}

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_ior_is_called(instance: Set) -> None:
    instance |= {2, 3}

    assert instance.length == 4
    assert instance == {0, 1, 2, 3}


def test_doesnt_change_value_if_hook_raised_error_when_ior_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance |= {2, 3}

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_isub_is_called(instance: Set) -> None:
    instance -= {0}

    assert instance.length == 2
    assert instance == {1, 2}


def test_doesnt_change_value_if_hook_raised_error_when_isub_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance -= {0}

    assert error_instance == {0, 1, 2}


def test_triggers_hook_when_ixor_is_called(instance: Set) -> None:
    instance ^= {1, 2, 3}

    assert instance.length == 2
    assert instance == {0, 3}


def test_doesnt_change_value_if_hook_raised_error_when_ixor_was_called(error_instance: ErrorSet) -> None:
    with pytest.raises(Exception):
        error_instance ^= {1, 2, 3}

    assert error_instance == {0, 1, 2}
