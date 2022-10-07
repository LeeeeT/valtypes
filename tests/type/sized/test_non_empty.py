import pytest

import valtypes.error.parsing.type.sized as error
import valtypes.type.sized as type


def test_empty() -> None:
    """
    It raises an error if the length equals to 0
    """

    class Sized(type.NonEmpty):
        def __len__(self) -> int:
            return 0

    with pytest.raises(error.MinimumLength) as info:
        Sized()

    assert info.value == error.MinimumLength(1, 0)


def test_non_empty() -> None:
    """
    It succeeds if the length is greater than 0
    """

    class Sized(type.NonEmpty):
        def __len__(self) -> int:
            return 1

    Sized()
