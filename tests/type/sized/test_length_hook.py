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


def test_instance_creation(instance: Sized) -> None:
    """
    It triggers the hook on instance creation
    """

    assert instance.length == 10


def test_notify_length_delta(instance: Sized) -> None:
    """
    It triggers the hook passing current object length + delta to it
    """

    instance.__notify_length_delta__(4)
    assert instance.length == 14


def test_notify_length_increments(instance: Sized) -> None:
    """
    It triggers the hook passing incremented object length to it
    """

    instance.__notify_length_increments__()
    assert instance.length == 11


def test_notify_length_decrements(instance: Sized) -> None:
    """
    It triggers the hook passing decremented object length to it
    """

    instance.__notify_length_decrements__()
    assert instance.length == 9
