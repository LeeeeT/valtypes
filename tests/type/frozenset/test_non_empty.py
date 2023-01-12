import pytest

import valtypes.error.parsing.sized as error
import valtypes.type.frozenset as type


def test_raises_error_if_value_is_empty() -> None:
    with pytest.raises(error.MinimumLength) as info:
        type.NonEmpty()

    assert info.value == error.MinimumLength(1, 0)


def test_succeeds_if_value_is_not_empty() -> None:
    type.NonEmpty({1})
