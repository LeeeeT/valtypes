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


def test_triggers_hook_when_clear_is_called(instance: List) -> None:
    instance.clear()

    assert instance.length == 0
    assert instance == []


def test_doesnt_change_value_if_hook_raised_error_when_clear_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance.clear()

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_append_is_called(instance: List) -> None:
    instance.append(3)

    assert instance.length == 4
    assert instance == [0, 1, 2, 3]


def test_doesnt_change_value_if_hook_raised_error_when_append_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance.append(3)

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_extend_is_called(instance: List) -> None:
    instance.extend(iter(range(3)))

    assert instance.length == 6
    assert instance == [0, 1, 2, 0, 1, 2]


def test_doesnt_change_value_if_hook_raised_error_when_extend_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance.extend(range(3))

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_pop_is_called(instance: List) -> None:
    assert instance.pop() == 2
    assert instance.length == 2
    assert instance == [0, 1]


def test_doesnt_change_value_if_hook_raised_error_when_pop_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance.pop()

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_insert_is_called(instance: List) -> None:
    instance.insert(0, -1)

    assert instance.length == 4
    assert instance == [-1, 0, 1, 2]


def test_doesnt_change_value_if_hook_raised_error_when_insert_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance.insert(0, -1)

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_remove_is_called(instance: List) -> None:
    instance.remove(2)

    assert instance.length == 2
    assert instance == [0, 1]


def test_doesnt_change_value_if_hook_raised_error_when_remove_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance.remove(2)

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_setitem_is_called_with_slice(instance: List) -> None:
    instance[:-1] = iter((3,))

    assert instance.length == 2
    assert instance == [3, 2]


def test_triggers_hook_when_setitem_is_called_with_not_slice(instance: List) -> None:
    instance[-1] = 0

    assert instance.length is None


def test_doesnt_change_value_if_hook_raised_error_when_setitem_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance[:-1] = (3,)

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_delitem_is_called_with_slice(instance: List) -> None:
    del instance[:-1]

    assert instance.length == 1
    assert instance == [2]


def test_triggers_hook_when_delitem_is_called_with_not_slice(instance: List) -> None:
    del instance[-1]

    assert instance.length == 2
    assert instance == [0, 1]


def test_doesnt_change_value_if_hook_raised_error_when_delitem_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        del error_instance[-1]

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_iadd_is_called(instance: List) -> None:
    instance += iter(range(2))

    assert instance.length == 5
    assert instance == [0, 1, 2, 0, 1]


def test_doesnt_change_value_if_hook_raised_error_when_iadd_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance += range(2)

    assert error_instance == [0, 1, 2]


def test_triggers_hook_when_imul_is_called(instance: List) -> None:
    instance *= 3

    assert instance.length == 9
    assert instance == [0, 1, 2, 0, 1, 2, 0, 1, 2]


def test_doesnt_change_value_if_hook_raised_error_when_imul_was_called(error_instance: ErrorClass) -> None:
    with pytest.raises(Exception):
        error_instance *= 3

    assert error_instance == [0, 1, 2]
