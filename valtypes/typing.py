import types
from array import array
from mmap import mmap
from pickle import PickleBuffer
from types import UnionType
from typing import TYPE_CHECKING, Any, Protocol, TypeVar, Union
from typing import _AnnotatedAlias as TypingAnnotatedAlias  # type: ignore
from typing import _GenericAlias as TypingGenericAlias  # type: ignore
from typing import _LiteralGenericAlias as LiteralGenericAlias  # type: ignore
from typing import _UnionGenericAlias as UnionGenericAlias  # type: ignore
from typing import runtime_checkable

if TYPE_CHECKING:
    from ctypes import _CData as CData  # type: ignore


__all__ = [
    "AnnotatedAlias",
    "Dataclass",
    "Descriptor",
    "GenericAlias",
    "LiteralAlias",
    "ReadableBuffer",
    "SupportsTrunc",
    "UnionAlias",
]


T_co = TypeVar("T_co", covariant=True)


class SupportsTrunc(Protocol):
    def __trunc__(self) -> int:
        ...


@runtime_checkable
class Descriptor(Protocol[T_co]):
    def __get__(self, instance: object, owner: type | None = ...) -> T_co:
        ...


ReadOnlyBuffer = bytes


WritableBuffer = Union[bytearray, memoryview, "array[Any]", mmap, "CData", PickleBuffer]


ReadableBuffer = ReadOnlyBuffer | WritableBuffer


Dataclass = Any


if TYPE_CHECKING:
    GenericAlias = Any
else:
    GenericAlias = TypingGenericAlias | types.GenericAlias


if TYPE_CHECKING:
    UnionAlias = UnionType
else:
    UnionAlias = UnionGenericAlias | UnionType


if TYPE_CHECKING:
    LiteralAlias = UnionType
else:
    LiteralAlias = LiteralGenericAlias


if TYPE_CHECKING:
    AnnotatedAlias = UnionType
else:
    AnnotatedAlias = TypingAnnotatedAlias
