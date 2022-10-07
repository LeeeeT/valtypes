from collections.abc import Callable, Iterable, Iterator, Sequence, Sized
from functools import cache, cached_property
from types import TracebackType
from typing import Any, Generic, ParamSpec, TypeVar, cast

from valtypes.typing import Descriptor, GenericAlias, LruCacheWrapper

__all__ = [
    "Binder",
    "CompositeBinder",
    "CompositeCallable",
    "CompositeCallableDescriptor",
    "ErrorsCollector",
    "cached_method",
    "ensure_iterable_not_iterator",
    "ensure_sequence",
    "get_slice_length",
    "pretty_type_repr",
]


P = ParamSpec("P")


T = TypeVar("T")

T_BaseException = TypeVar("T_BaseException", bound=BaseException)

T_ErrorsCollector = TypeVar("T_ErrorsCollector", bound="ErrorsCollector[Any]")


type_ = type


class Binder(Generic[T]):
    def __init__(self, object: Descriptor[T] | T):
        self._object = object

    def bind(self, instance: object, owner: type | None) -> T:
        if isinstance(self._object, Descriptor):
            return cast(Descriptor[T], self._object).__get__(instance, owner)
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


class ErrorsCollector(Generic[T_BaseException]):
    def __init__(self, *types: type[T_BaseException]):
        self._types = types

    @cached_property
    def _errors(self) -> list[T_BaseException]:
        return []

    def __enter__(self: T_ErrorsCollector) -> T_ErrorsCollector:
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None:
        if isinstance(exc_val, self._types):
            self._errors.append(cast(T_BaseException, exc_val))
            return True

    def __iter__(self) -> Iterator[T_BaseException]:
        return iter(self._errors)

    def __bool__(self) -> bool:
        return bool(self._errors)


def pretty_type_repr(type: object, /) -> str:
    if isinstance(type, GenericAlias):
        return pretty_type_repr(type.__origin__) + "[" + ", ".join(pretty_type_repr(arg) for arg in type.__args__) + "]"
    if isinstance(type, type_):
        return type.__name__
    return repr(type)


def ensure_iterable_not_iterator(iterable: Iterable[T]) -> Iterable[T]:
    if isinstance(iterable, Iterator):
        return tuple(cast(Iterator[T], iterable))
    return iterable


def ensure_sequence(iterable: Iterable[T]) -> Sequence[T]:
    if isinstance(iterable, Sequence):
        return iterable
    return tuple(iterable)


def get_slice_length(slice: slice, sized: Sized) -> int:
    return len(range(*slice.indices(len(sized))))


def cached_method(method: Callable[..., T]) -> cached_property[LruCacheWrapper[T]]:
    def getter(self: object) -> LruCacheWrapper[T]:
        return cache(method.__get__(self))

    return cached_property(getter)
