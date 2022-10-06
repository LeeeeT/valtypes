from collections.abc import Iterable, Set
from typing import Any, Generic, TypeVar

from valtypes.util import ensure_iterable_not_iterator

from . import generic, sized

__all__ = ["InitHook", "LengthHook", "MaximumLength", "MinimumLength", "NonEmpty"]


T = TypeVar("T")

T_LengthHook = TypeVar("T_LengthHook", bound="LengthHook[Any]")


class InitHook(generic.InitHook, set[T], Generic[T]):
    def __init__(self, iterable: Iterable[T] = set(), /):
        super().__init__(iterable)


class LengthHook(InitHook[T], sized.LengthHook, Generic[T]):
    def add(self, element: T, /) -> None:
        if element not in self:
            self.__notify_length_increments__()
        super().add(element)

    def difference_update(self, *iterables: Iterable[Any]) -> None:
        iterables = tuple(ensure_iterable_not_iterator(iterable) for iterable in iterables)
        self.__length_hook__(len(self.difference(*iterables)))
        super().difference_update(*iterables)

    def discard(self, element: T, /) -> None:
        if element in self:
            self.__notify_length_decrements__()
        super().discard(element)

    def intersection_update(self, *iterables: Iterable[Any]) -> None:
        iterables = tuple(ensure_iterable_not_iterator(iterable) for iterable in iterables)
        self.__length_hook__(len(self.intersection(*iterables)))
        super().intersection_update(*iterables)

    def clear(self) -> None:
        self.__length_hook__(0)
        super().clear()

    def pop(self) -> T:
        self.__notify_length_decrements__()
        return super().pop()

    def remove(self, element: T, /) -> None:
        self.__notify_length_decrements__()
        super().remove(element)

    def symmetric_difference_update(self, iterable: Iterable[T], /) -> None:
        iterable = ensure_iterable_not_iterator(iterable)
        self.__length_hook__(len(self.symmetric_difference(iterable)))
        super().symmetric_difference_update(iterable)

    def update(self, *iterables: Iterable[T]) -> None:
        iterables = tuple(ensure_iterable_not_iterator(iterable) for iterable in iterables)
        self.__length_hook__(len(self.union(*iterables)))
        super().update(*iterables)

    def __iand__(self: T_LengthHook, other: Set[object], /) -> T_LengthHook:
        self.__length_hook__(len(self & other))
        return super().__iand__(other)

    def __ior__(self: T_LengthHook, other: Set[T], /) -> T_LengthHook:  # type: ignore
        self.__length_hook__(len(self | other))
        return super().__ior__(other)

    def __isub__(self: T_LengthHook, other: Set[object], /) -> T_LengthHook:
        self.__length_hook__(len(self - other))
        return super().__isub__(other)

    def __ixor__(self: T_LengthHook, other: Set[T], /) -> T_LengthHook:  # type: ignore
        self.__length_hook__(len(self ^ other))
        return super().__ixor__(other)


class MinimumLength(LengthHook[T], sized.MinimumLength, Generic[T]):
    pass


class MaximumLength(LengthHook[T], sized.MaximumLength, Generic[T]):
    pass


class NonEmpty(LengthHook[T], sized.NonEmpty, Generic[T]):
    pass
