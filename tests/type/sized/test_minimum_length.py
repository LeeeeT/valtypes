import pytest

import valtypes.error.parsing.sized as error
import valtypes.type.sized as type


def test_raises_error_if_length_is_less_than_minimum() -> None:
    class Sized(type.MinimumLength):
        __minimum_length__ = 3

        def __len__(self) -> int:
            return 2

    with pytest.raises(error.MinimumLength) as info:
        Sized()

    assert info.value == error.MinimumLength(3, 2)


def test_succeeds_if_length_equals_to_minimum() -> None:
    class Sized(type.MinimumLength):
        __minimum_length__ = 3

        def __len__(self) -> int:
            return 3

    Sized()


def test_succeeds_if_length_is_greater_than_minimum() -> None:
    class Sized(type.MinimumLength):
        __minimum_length__ = 3

        def __len__(self) -> int:
            return 4

    Sized()
