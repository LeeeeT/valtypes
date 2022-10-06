import pytest

import valtypes.error.sized as error
import valtypes.type.set as type


def test_less() -> None:
    """
    It raises an error if the length is less than the allowed minimum
    """

    class Set(type.MinimumLength[object]):
        __minimum_length__ = 3

        def __len__(self) -> int:
            return 2

    with pytest.raises(error.MinimumLength) as info:
        Set()

    assert info.value == error.MinimumLength(3, 2)


def test_equals() -> None:
    """
    It succeeds if the length equals to the allowed minimum
    """

    class Set(type.MinimumLength[object]):
        __minimum_length__ = 3

        def __len__(self) -> int:
            return 3

    Set()


def test_greater() -> None:
    """
    It succeeds if the length is greater than the allowed minimum
    """

    class Set(type.MinimumLength[object]):
        __minimum_length__ = 3

        def __len__(self) -> int:
            return 4

    Set()
