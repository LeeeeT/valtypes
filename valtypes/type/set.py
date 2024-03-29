from collections.abc import Iterable, Set
from typing import Any, Self, TypeVar

from valtypes.util import ensure_iterable_not_iterator

from . import generic, sized

__all__ = ["InitHook", "LengthHook", "MaximumLength", "MinimumLength", "NonEmpty"]


T = TypeVar("T")


class InitHook(generic.InitHook, set[T]):
    def __init__(self, iterable: Iterable[T] = set(), /):
        super().__init__(iterable)


class LengthHook(InitHook[T], sized.LengthHook):
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

    def __iand__(self, other: Set[object], /) -> Self:
        self.__length_hook__(len(self & other))
        return super().__iand__(other)

    def __ior__(self, other: Set[T], /) -> Self:
        self.__length_hook__(len(self | other))
        return super().__ior__(other)

    def __isub__(self, other: Set[Any], /) -> Self:
        self.__length_hook__(len(self - other))
        return super().__isub__(other)

    def __ixor__(self, other: Set[T], /) -> Self:
        self.__length_hook__(len(self ^ other))
        return super().__ixor__(other)


class MinimumLength(LengthHook[T], sized.MinimumLength):
    pass


class MaximumLength(LengthHook[T], sized.MaximumLength):
    pass


class NonEmpty(LengthHook[T], sized.NonEmpty):
    pass
