from types import GenericAlias as TypesGenericAlias
from types import UnionType as TypesUnionType
from typing import Protocol, SupportsFloat, SupportsIndex, TypeVar
from typing import _GenericAlias as TypingGenericAlias  # type: ignore
from typing import _UnionGenericAlias as TypingUnionType  # type: ignore

__all__ = [
    "Floatable",
    "GenericAlias",
    "SupportsGe",
    "SupportsGt",
    "SupportsLe",
    "SupportsLt",
    "UnionType",
]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


Floatable = SupportsIndex | SupportsFloat | bytes | bytearray | str


GenericAlias = TypingGenericAlias | TypesGenericAlias


UnionType = TypingUnionType | TypesUnionType


class SupportsLt(Protocol[T_contra]):
    def __lt__(self, other: T_contra, /) -> bool:
        ...


class SupportsLe(Protocol[T_contra]):
    def __le__(self, other: T_contra, /) -> bool:
        ...


class SupportsGt(Protocol[T_contra]):
    def __gt__(self, other: T_contra, /) -> bool:
        ...


class SupportsGe(Protocol[T_contra]):
    def __ge__(self, other: T_contra, /) -> bool:
        ...
