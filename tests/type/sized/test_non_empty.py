import pytest

import valtypes.error.parsing.sized as error
import valtypes.type.sized as type


def test_raises_error_if_value_is_empty() -> None:
    class Sized(type.NonEmpty):
        def __len__(self) -> int:
            return 0

    with pytest.raises(error.MinimumLength) as info:
        Sized()

    assert info.value == error.MinimumLength(1, 0)


def test_succeeds_if_value_is_not_empty() -> None:
    class Sized(type.NonEmpty):
        def __len__(self) -> int:
            return 1

    Sized()
