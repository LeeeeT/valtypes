from typing import Generic, TypeVar

from valtypes import Constrained, condition, parse

T = TypeVar("T")


def test_pass_to_init() -> None:
    """
    It triggers the constraint
    """

    constraint_triggered = False

    def constraint(value: object, /) -> bool:
        nonlocal constraint_triggered
        constraint_triggered = True
        return True

    class MyConstrained(Constrained[object]):
        __constraint__ = constraint

    parse(MyConstrained, 1)

    assert constraint_triggered


def test_parse_to_bound() -> None:
    """
    It parses a value to the bound of a constrained before creating an instance
    """

    class ConstrainedFloat(Constrained[float]):
        __constraint__ = condition.true

    assert isinstance(parse(ConstrainedFloat, "inf"), float)


def test_resolve_bound_type_args() -> None:
    """
    It resolves type arguments of the bound of a constrained
    """

    class MyList(Constrained[list[T]], list[T], Generic[T]):
        __constraint__ = condition.true

    assert parse(MyList[object], range(3)) == [0, 1, 2]
    assert parse(MyList[bytes], range(3)) == [b"0", b"1", b"2"]
