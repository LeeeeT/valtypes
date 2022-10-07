import pytest

import valtypes.error.parsing.type.sized as error
import valtypes.type.list as type


def test_empty() -> None:
    """
    It raises an error if the length equals to 0
    """

    with pytest.raises(error.MinimumLength) as info:
        type.NonEmpty()

    assert info.value == error.MinimumLength(1, 0)


def test_non_empty() -> None:
    """
    It succeeds if the length is greater than 0
    """

    type.NonEmpty([1])
