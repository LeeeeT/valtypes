from typing import Generic, TypeVar

from valtypes import Constrained

__all__ = ["NonEmptyFrozenset", "NonEmptyList", "NonEmptySet", "NonEmptyTuple"]


T = TypeVar("T")


class NonEmptyList(Constrained[list[T]], list[T], Generic[T]):
    __constraint__ = bool


class NonEmptyTuple(Constrained[tuple[T, ...]], tuple[T, ...], Generic[T]):
    __constraint__ = bool


class NonEmptySet(Constrained[set[T]], set[T], Generic[T]):
    __constraint__ = bool


class NonEmptyFrozenset(Constrained[frozenset[T]], frozenset[T], Generic[T]):
    __constraint__ = bool
