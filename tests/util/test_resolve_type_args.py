from types import NoneType
from typing import Generic, TypeVar

from valtypes.util import resolve_type_args


def test_non_generic() -> None:
    """
    It should return empty tuple for non-generic types
    """

    assert resolve_type_args(tuple, tuple) == ()


def test_parameterized_builtin_type() -> None:
    """
    It should return type args of parameterized built-in types
    """

    assert resolve_type_args(list[int], list) == (int,)
    assert resolve_type_args(tuple[int, bytes, str], tuple) == (int, bytes, str)  # type: ignore


def test_target_class_not_found() -> None:
    """
    It should return empty tuple if target class not found in the bases of a class
    """

    assert resolve_type_args(list[int], tuple) == ()


def test_subclass_of_parameterized_builtin_type() -> None:
    """
    It should recursively find parameterized built-in types in the bases of a class
    """

    class MyTuple(tuple[float, bytes, None]):
        pass

    class MyTupleSubclass(MyTuple):
        pass

    assert resolve_type_args(MyTuple, tuple) == (float, bytes, None)
    assert resolve_type_args(MyTupleSubclass, tuple) == (float, bytes, None)


def test_parameterized_generic() -> None:
    """
    It should collect type args from a parameterized generic
    """

    T = TypeVar("T")
    F = TypeVar("F")
    S = TypeVar("S")

    class MyGeneric(Generic[T, F, S]):
        pass

    assert resolve_type_args(MyGeneric[None, int, float], MyGeneric) == (NoneType, int, float)


def test_non_parameterized_generic() -> None:
    """
    It should return type vars' bounds for a non-parameterized generic
    """

    T = TypeVar("T", bound=int)
    F = TypeVar("F", str, bytes)
    S = TypeVar("S")

    class MyGeneric(Generic[T, F, S]):
        pass

    assert resolve_type_args(MyGeneric, MyGeneric) == (int, str | bytes, object)


def test_partially_parameterized_generic() -> None:
    """
    It should restore missing type args with corresponding type vars' bounds in partially parameterized generic
    """

    T = TypeVar("T", bound=float)
    F = TypeVar("F")
    S = TypeVar("S", bound=int)

    class MyGeneric(Generic[T, F]):
        pass

    assert resolve_type_args(MyGeneric[S, str], MyGeneric) == (int, str)


def test_type_args_propagation() -> None:
    """
    It should propagate type args to the generic's bases
    """

    T = TypeVar("T", bound=float)
    F = TypeVar("F", str, bytes)
    S = TypeVar("S")

    class MyTuple(tuple[T, ...], Generic[F, T]):
        pass

    class MyTupleSubclass(MyTuple[str, T], Generic[T, S]):
        pass

    assert resolve_type_args(MyTuple[str, int], tuple) == (int, ...)
    assert resolve_type_args(MyTuple, tuple) == (float, ...)
    assert resolve_type_args(MyTupleSubclass, MyTuple) == (str, float)
    assert resolve_type_args(MyTupleSubclass[bool], tuple) == (bool, ...)  # type: ignore
