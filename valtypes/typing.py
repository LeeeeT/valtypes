from types import GenericAlias as TypesGenericAlias
from typing import Protocol, SupportsFloat, SupportsIndex, TypeVar
from typing import _GenericAlias as TypingGenericAlias  # type: ignore  # noqa

__all__ = [
    "Floatable",
    "GenericAlias",
    "SupportsGetItem",
    "SupportsGe",
    "SupportsGt",
    "SupportsLe",
    "SupportsLt",
    "SupportsMod",
    "HasModuleAndName",
]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


Floatable = SupportsFloat | SupportsIndex | str | bytes | bytearray


GenericAlias = TypingGenericAlias | TypesGenericAlias


class SupportsGetItem(Protocol[T_contra, T_co]):
    def __getitem__(self, item: T_contra, /) -> T_co:
        ...


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


class SupportsMod(Protocol[T_contra, T_co]):
    def __mod__(self, other: T_contra, /) -> T_co:
        ...


class HasModuleAndName(Protocol):
    __module__: str
    __name__: str
