import pytest

import valtypes.error.parsing.sized as error
import valtypes.type.sized as type


def test_raises_error_if_length_is_greater_than_maximum() -> None:
    class Sized(type.MaximumLength):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 3

    with pytest.raises(error.MaximumLength) as info:
        Sized()

    assert info.value == error.MaximumLength(2, 3)


def test_succeeds_if_length_equals_to_maximum() -> None:
    class Sized(type.MaximumLength):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 2

    Sized()


def test_succeeds_if_length_is_less_than_maximum() -> None:
    class Sized(type.MaximumLength):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 1

    Sized()
