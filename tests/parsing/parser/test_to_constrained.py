from typing import Generic, TypeVar

import pytest

from valtypes import BaseParsingError, Constrained, condition, parse
from valtypes.type.numeric import Portion

T = TypeVar("T")


def test_parse_to_bound() -> None:
    """
    It parses the value to the bound of the constrained before creating an instance
    """

    class Float(Constrained[float]):
        __constraint__ = condition.true

    assert isinstance(parse(Float, "inf"), float)


def test_resolve_bound_type_args() -> None:
    """
    It resolves the type argument of the bound of the constrained
    """

    class MyList(Constrained[list[T]], list[T], Generic[T]):
        __constraint__ = condition.true

    assert parse(MyList[object], range(3)) == [0, 1, 2]
    assert parse(MyList[bytes], range(3)) == [b"0", b"1", b"2"]


def test_error() -> None:
    """
    It raises an error if the value doesn't match the constraint
    """

    with pytest.raises(BaseParsingError):
        parse(Portion, 2)
