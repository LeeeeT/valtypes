from typing import Generic, TypeVar

import pytest

from valtypes.util import resolve_type_args


def test_parameterized_builtin_type() -> None:
    """
    It returns the type arguments of parameterized built-in types
    """

    assert resolve_type_args(list[int], list) == (int,)
    assert resolve_type_args(tuple[int, bytes, str], tuple) == (int, bytes, str)  # type: ignore


def test_subclass_of_parameterized_builtin_type() -> None:
    """
    It finds parameterized built-in types in the bases of the class
    """

    class Tuple(tuple[float, bytes, None]):
        pass

    class TupleSubclass(Tuple):
        pass

    assert resolve_type_args(Tuple, tuple) == (float, bytes, None)
    assert resolve_type_args(TupleSubclass, tuple) == (float, bytes, None)


def test_type_args_propagation() -> None:
    """
    It propagates type arguments to the generic's bases
    """

    T = TypeVar("T", bound=float)
    F = TypeVar("F", str, bytes)
    S = TypeVar("S")

    class Tuple(tuple[T, ...], Generic[F, T]):
        pass

    class TupleSubclass(Tuple[str, T], Generic[T, S]):
        pass

    assert resolve_type_args(Tuple[str, int], tuple) == (int, ...)
    assert resolve_type_args(TupleSubclass[int, bytes], Tuple) == (str, int)
    assert resolve_type_args(TupleSubclass[bool, None], tuple) == (bool, ...)


def test_not_generic() -> None:
    """
    It raises an error if the target class isn't a generic
    """

    with pytest.raises(TypeError):
        resolve_type_args(tuple, tuple)


def test_target_not_in_bases() -> None:
    """
    It raises an error if the target class isn't in the bases of the origin class
    """

    with pytest.raises(TypeError):
        resolve_type_args(list[int], tuple)
