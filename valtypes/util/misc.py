from collections.abc import Callable, Iterable, Iterator, Sequence, Sized
from typing import Generic, ParamSpec, TypeVar
from typing import _type_repr as typing_type_repr  # type: ignore

from valtypes.typing import Descriptor

__all__ = [
    "Binder",
    "CompositeBinder",
    "CompositeCallable",
    "CompositeCallableDescriptor",
    "ensure_iterable_not_iterator",
    "ensure_sequence",
    "get_slice_length",
    "type_repr",
]


P = ParamSpec("P")

T = TypeVar("T")


class Binder(Generic[T]):
    def __init__(self, object: Descriptor[T] | T):
        self._object = object

    def bind(self, instance: object, owner: type | None) -> T:
        if isinstance(self._object, Descriptor):
            return self._object.__get__(instance, owner)
        return self._object


class CompositeBinder(Generic[T]):
    def __init__(self, objects: Iterable[Descriptor[T] | T]):
        self._binders = [Binder(object) for object in objects]

    def bind(self, instance: object, owner: type | None) -> list[T]:
        return [binder.bind(instance, owner) for binder in self._binders]


class CompositeCallable(Generic[P]):
    def __init__(self, callables: Iterable[Callable[P, object]]):
        self._callables = callables

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> None:
        for callable in self._callables:
            callable(*args, **kwargs)


class CompositeCallableDescriptor(Generic[P]):
    def __init__(self, callables: Iterable[Descriptor[Callable[P, object]] | Callable[P, object]]):
        self._binder = CompositeBinder(callables)

    def __get__(self, instance: object, owner: type | None = None) -> Callable[P, None]:
        return CompositeCallable[P](self._binder.bind(instance, owner))


def type_repr(type: object) -> str:
    return typing_type_repr(type)


def ensure_iterable_not_iterator(iterable: Iterable[T]) -> Iterable[T]:
    if isinstance(iterable, Iterator):
        return tuple(iterable)
    return iterable


def ensure_sequence(iterable: Iterable[T]) -> Sequence[T]:
    if isinstance(iterable, Sequence):
        return iterable
    return tuple(iterable)


def get_slice_length(slice: slice, sized: Sized) -> int:
    return len(range(*slice.indices(len(sized))))
