import functools
import types
import typing
from mmap import mmap
from pickle import PickleBuffer
from types import UnionType
from typing import TYPE_CHECKING, Generic, Protocol, SupportsFloat, SupportsIndex, SupportsInt, TypeVar, runtime_checkable

__all__ = [
    "AnnotatedAlias",
    "Descriptor",
    "Floatable",
    "GenericAlias",
    "Intable",
    "LiteralAlias",
    "LruCacheWrapper",
    "ReadableBuffer",
    "SupportsTrunc",
    "UnionAlias",
]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class SupportsTrunc(Protocol):
    def __trunc__(self) -> int:
        ...


@runtime_checkable
class Descriptor(Protocol[T_co]):
    def __get__(self, instance: object, owner: type | None = ...) -> T_co:
        ...


ReadableBuffer = bytes | bytearray | memoryview | mmap | PickleBuffer


Intable = SupportsInt | SupportsIndex | SupportsTrunc | ReadableBuffer | str


Floatable = SupportsIndex | SupportsFloat | ReadableBuffer | str


if TYPE_CHECKING:
    GenericAlias = types.GenericAlias
else:
    GenericAlias = typing._GenericAlias | types.GenericAlias


if TYPE_CHECKING:
    UnionAlias = UnionType
else:
    UnionAlias = typing._UnionGenericAlias | UnionType


if TYPE_CHECKING:
    LiteralAlias = UnionType
else:
    LiteralAlias = typing._LiteralGenericAlias


if TYPE_CHECKING:
    AnnotatedAlias = UnionType
else:
    AnnotatedAlias = typing._AnnotatedAlias


if TYPE_CHECKING:
    LruCacheWrapper = functools._lru_cache_wrapper  # type: ignore
else:

    class LruCacheWrapper(Generic[T]):
        pass
