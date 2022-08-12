import pytest

import valtypes.error.sized as error
import valtypes.type.list as type


def test_greater() -> None:
    """
    It raises an error if the length is greater than the allowed maximum
    """

    class List(type.MaximumLength[object]):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 3

    with pytest.raises(error.MaximumLength) as info:
        List()

    assert info.value == error.MaximumLength(2, 3)


def test_equals() -> None:
    """
    It succeeds if the length equals to the allowed maximum
    """

    class List(type.MaximumLength[object]):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 2

    List()


def test_less() -> None:
    """
    It succeeds if the length is less than the allowed maximum
    """

    class List(type.MaximumLength[object]):
        __maximum_length__ = 2

        def __len__(self) -> int:
            return 1

    List()
