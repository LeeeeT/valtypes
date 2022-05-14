import pytest

from valtypes import Constrained, ConstraintError
from valtypes.condition import false, true


def test_constraint_returns_false() -> None:
    """
    It raises an error if the constraint returns False when creating an instance
    """

    class Class(Constrained[object]):
        __constraint__ = false

    with pytest.raises(ConstraintError):
        Class(...)


def test_constraint_returns_true() -> None:
    """
    It returns the value itself if the constraint returns True when creating an instance
    """

    class Class(Constrained[object]):
        __constraint__ = true

    assert Class(...) is ...  # type: ignore
