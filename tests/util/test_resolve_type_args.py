from typing import Any, Generic, TypeVar, cast

import pytest

from valtypes.util import resolve_type_args


def test_returns_type_arguments_of_parameterized_builtin_type() -> None:
    assert resolve_type_args(list[int], list) == (int,)
    assert resolve_type_args(cast(Any, tuple)[int, bytes, str], tuple) == (int, bytes, str)


def test_finds_parameterized_builtin_types_in_bases_of_class() -> None:
    class Tuple(tuple[float, bytes, None]):
        pass

    class TupleSubclass(Tuple):
        pass

    assert resolve_type_args(Tuple, tuple) == (float, bytes, None)
    assert resolve_type_args(TupleSubclass, tuple) == (float, bytes, None)


def test_propagates_type_arguments_to_bases_of_generic_class() -> None:
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


def test_raises_error_if_target_class_isnt_generic() -> None:
    with pytest.raises(TypeError):
        resolve_type_args(tuple, tuple)


def test_raises_error_if_target_class_isnt_in_bases_of_origin_class() -> None:
    with pytest.raises(TypeError):
        resolve_type_args(list[int], tuple)
