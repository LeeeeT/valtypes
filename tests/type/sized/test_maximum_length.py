import pytest

import valtypes.error.parsing.type.sized as error
import valtypes.type.sized as type


def test_greater() -> None:
    """
    It raises an error if the length is greater than the allowed maximum
    """

    class Sized(type.MaximumLength):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 3

    with pytest.raises(error.MaximumLength) as info:
        Sized()

    assert info.value == error.MaximumLength(2, 3)


def test_equals() -> None:
    """
    It succeeds if the length equals to the allowed maximum
    """

    class Sized(type.MaximumLength):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 2

    Sized()


def test_less() -> None:
    """
    It succeeds if the length is less than the allowed maximum
    """

    class Sized(type.MaximumLength):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 1

    Sized()
