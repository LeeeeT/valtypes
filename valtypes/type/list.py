from collections.abc import Iterable
from typing import Any, Generic, SupportsIndex, TypeVar, cast, overload

from valtypes.util import ensure_sequence, get_slice_length

from . import generic, sized

__all__ = ["InitHook", "LengthHook", "MaximumLength", "MinimumLength", "NonEmpty"]


T = TypeVar("T")

T_LengthHook = TypeVar("T_LengthHook", bound="LengthHook[Any]")


class InitHook(generic.InitHook, list[T], Generic[T]):
    def __init__(self, iterable: Iterable[T] = [], /):
        super().__init__(iterable)


class LengthHook(InitHook[T], sized.LengthHook, Generic[T]):
    def clear(self) -> None:
        self.__length_hook__(0)
        super().clear()

    def append(self, value: T, /) -> None:
        self.__notify_length_increments__()
        super().append(value)

    def extend(self, iterable: Iterable[T], /) -> None:
        sequence = ensure_sequence(iterable)
        self.__notify_length_delta__(len(sequence))
        super().extend(sequence)

    def pop(self, index: SupportsIndex = -1, /) -> T:
        self.__notify_length_decrements__()
        return super().pop(index)

    def insert(self, index: SupportsIndex, value: T, /) -> None:
        self.__notify_length_increments__()
        super().insert(index, value)

    def remove(self, value: T, /) -> None:
        self.__notify_length_decrements__()
        super().remove(value)

    @overload
    def __setitem__(self, index: SupportsIndex, value: T, /) -> None:
        ...

    @overload
    def __setitem__(self, slice: slice, iterable: Iterable[T], /) -> None:
        ...

    def __setitem__(self, item: SupportsIndex | slice, object: T | Iterable[T], /) -> None:
        if isinstance(item, slice):
            object = ensure_sequence(cast(Iterable[T], object))
            self.__notify_length_delta__(len(object) - get_slice_length(item, self))
        super().__setitem__(cast(Any, item), cast(Any, object))

    def __delitem__(self, item: SupportsIndex | slice, /) -> None:
        if isinstance(item, slice):
            self.__notify_length_delta__(-get_slice_length(item, self))
        else:
            self.__notify_length_decrements__()
        super().__delitem__(item)

    def __iadd__(self: T_LengthHook, iterable: Iterable[T], /) -> T_LengthHook:
        sequence = ensure_sequence(iterable)
        self.__notify_length_delta__(len(sequence))
        return super().__iadd__(sequence)

    def __imul__(self: T_LengthHook, multiplier: SupportsIndex, /) -> T_LengthHook:
        self.__length_hook__(len(self) * int(multiplier))
        return super().__imul__(multiplier)


class MinimumLength(LengthHook[T], sized.MinimumLength, Generic[T]):
    pass


class MaximumLength(LengthHook[T], sized.MaximumLength, Generic[T]):
    pass


class NonEmpty(MinimumLength[T], sized.NonEmpty, Generic[T]):
    pass
