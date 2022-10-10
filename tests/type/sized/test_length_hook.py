import pytest

import valtypes.type.sized as type


class Sized(type.LengthHook):
    length: int

    def __length_hook__(self, length: int) -> None:
        self.length = length

    def __len__(self) -> int:
        return 10


@pytest.fixture
def instance() -> Sized:
    return Sized()


def test_triggers_hook_on_instance_creation(instance: Sized) -> None:
    assert instance.length == 10


def test_notify_length_delta_passes_current_length_plus_delta_to_hook(instance: Sized) -> None:
    instance.__notify_length_delta__(4)
    assert instance.length == 14


def test_notify_length_increments_passes_incremented_length_to_hook(instance: Sized) -> None:
    instance.__notify_length_increments__()
    assert instance.length == 11


def test_notify_length_decrements_passes_decremented_length_to_hook(instance: Sized) -> None:
    instance.__notify_length_decrements__()
    assert instance.length == 9
