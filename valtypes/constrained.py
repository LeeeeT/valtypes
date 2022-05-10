from collections.abc import Callable
from typing import Any, Generic, TypeGuard, TypeVar

from .error import ConstraintError

__all__ = ["Constrained"]


T = TypeVar("T")

T_Constrained = TypeVar("T_Constrained", bound="Constrained[Any]")


class Constrained(Generic[T]):
    __constraint__: Callable[[T], bool]

    def __new__(cls: type[T_Constrained], value: T, /) -> T_Constrained:
        if cls.check(value):
            return value  # type: ignore
        raise ConstraintError(value, cls)

    @classmethod
    def check(cls: type[T_Constrained], value: T) -> TypeGuard[T_Constrained]:
        return cls.__constraint__(value)
