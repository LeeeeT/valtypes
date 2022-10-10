import pytest

import valtypes.error.parsing.type.sized as error
import valtypes.type.set as type


def test_raises_error_if_length_is_greater_than_maximum() -> None:
    class Set(type.MaximumLength[object]):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 3

    with pytest.raises(error.MaximumLength) as info:
        Set()

    assert info.value == error.MaximumLength(2, 3)


def test_succeeds_if_length_equals_to_maximum() -> None:
    class Set(type.MaximumLength[object]):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 2

    Set()


def test_succeeds_if_length_is_less_than_maximum() -> None:
    class Set(type.MaximumLength[object]):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 1

    Set()
