from typing import Generic, TypeVar

from . import condition
from .error import ConstraintError
from .util import get_absolute_name

__all__ = ["Constrained"]


T = TypeVar("T")


class Constrained(Generic[T]):
    __constraint__: condition.ABC[T]

    def __init__(self, value: T, /):
        if not self.__full_constraint__.check(value):
            raise ConstraintError(value, self.__full_constraint__)

    @classmethod
    @property
    def __full_constraint__(cls) -> condition.ABC[T]:
        return condition.And(
            *(
                base.__constraint__
                for base in reversed(cls.mro())
                if issubclass(base, Constrained) and "__constraint__" in base.__dict__
            )
        )

    def __str__(self) -> str:
        return self if isinstance(self, str) else super().__repr__()

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({super().__repr__()})"  # type: ignore
