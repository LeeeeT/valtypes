from __future__ import annotations

from typing import Generic, TypeVar

from . import condition
from .error import ConstraintError
from .util import SuppressSlotsMeta, get_absolute_name

__all__ = ["ConstrainedMeta", "Constrained"]


T_co = TypeVar("T_co", covariant=True)


class ConstrainedMeta(SuppressSlotsMeta):
    def __init__(cls, name: str, bases: tuple[type, ...], attrs: dict[str, object]):
        super().__init__(name, bases, attrs)
        if "_constraint" not in attrs:
            cls._constraint = condition.truthy


class Constrained(Generic[T_co], metaclass=ConstrainedMeta):
    _constraint: condition.ABC[T_co]

    @classmethod
    def __init__(cls, value: T_co, /):
        constraints = reversed([base._constraint for base in cls.mro() if issubclass(base, Constrained)])
        for constraint in constraints:
            if not constraint.check(value):
                raise ConstraintError(value, constraint)

    def __str__(self) -> str:
        return self if isinstance(self, str) else super().__repr__()

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({super().__repr__()})"
