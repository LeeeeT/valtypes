from __future__ import annotations

import abc
from collections.abc import Container
from types import UnionType
from typing import Any, Callable, Generic, TypeVar

import regex

from . import decorator
from .typing import SupportsGe, SupportsGt, SupportsLe, SupportsLt
from .util import get_absolute_name

__all__ = [
    "ABC",
    "And",
    "Or",
    "Not",
    "Decorated",
    "FromCallable",
    "Is",
    "IsInstance",
    "IsSubclass",
    "Equals",
    "LowerThan",
    "LowerEquals",
    "GreaterThan",
    "GreaterEquals",
    "Range",
    "Contains",
    "In",
    "Pattern",
    "positive",
    "negative",
    "non_positive",
    "non_negative",
    "convert",
    "truthy",
    "falsy",
]

T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)

F = TypeVar("F")


class ABC(abc.ABC, Generic[T_contra]):
    @abc.abstractmethod
    def check(self, value: T_contra, /) -> bool:
        pass

    def __and__(self, other: ABC[Any]) -> And[T_contra]:
        return And(self, other)

    def __or__(self, other: ABC[T_contra]) -> Or[T_contra]:
        return Or(self, other)

    def __invert__(self) -> Not[T_contra]:
        return Not(self)

    def __rrshift__(self, other: decorator.ABC[T, T_contra] | Callable[[T], T_contra]) -> ABC[T]:
        if not isinstance(other, decorator.ABC) and not callable(other):
            return NotImplemented
        if not isinstance(other, decorator.ABC):
            other = decorator.FromCallable(other)
        return Decorated(other, self)


class And(ABC[T], Generic[T]):
    def __init__(self, *conditions: ABC[T]):
        self.conditions = conditions

    def check(self, value: T, /) -> bool:
        return all(condition.check(value) for condition in self.conditions)

    def __repr__(self) -> str:
        if not self.conditions:
            return f"*{truthy!r}"
        if len(self.conditions) == 1:
            return f"*{self.conditions[0]!r}"
        return f"({' & '.join(map(repr, self.conditions))})"


class Or(ABC[T], Generic[T]):
    def __init__(self, *conditions: ABC[T]):
        self.conditions = conditions

    def check(self, value: T, /) -> bool:
        return any(condition.check(value) for condition in self.conditions)

    def __repr__(self) -> str:
        if not self.conditions:
            return f"*{falsy!r}"
        if len(self.conditions) == 1:
            return f"*{self.conditions[0]!r}"
        return f"({' | '.join(map(repr, self.conditions))})"


class Not(ABC[T], Generic[T]):
    def __init__(self, condition: ABC[T], /):
        self.condition = condition

    def check(self, value: T, /) -> bool:
        return not self.condition.check(value)

    def __repr__(self) -> str:
        return f"~{self.condition!r}"


class Decorated(ABC[T], Generic[T]):
    def __init__(self, decorator: decorator.ABC[T, F], condition: ABC[F]):
        self.decorator = decorator
        self.condition = condition

    def check(self, value: T, /) -> bool:
        return self.condition.check(self.decorator.decorate(value))

    def __repr__(self) -> str:
        return f"{self.decorator!r} >> {self.condition!r}"


class FromCallable(ABC[T], Generic[T]):
    def __init__(self, callable: Callable[[T], bool], /):
        self.callable = callable

    def check(self, value: T, /) -> bool:
        return self.callable(value)

    def __repr__(self) -> str:
        return get_absolute_name(self.callable)


class Is(ABC[object]):
    def __init__(self, obj: object, /):
        self.object = obj

    def check(self, value: object, /) -> bool:
        return value is self.object

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.object!r})"


class IsInstance(ABC[object]):
    def __init__(self, *types: type | UnionType):
        self.types = types

    def check(self, value: object, /) -> bool:
        return isinstance(value, self.types)

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({', '.join(map(repr, self.types))})"


class IsSubclass(ABC[type]):
    def __init__(self, *types: type | UnionType):
        self.types = types

    def check(self, value: type, /) -> bool:
        return issubclass(value, self.types)

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({', '.join(map(repr, self.types))})"


class Equals(ABC[object]):
    def __init__(self, obj: object, /):
        self.object = obj

    def check(self, value: object, /) -> bool:
        return value == self.object

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.object!r})"


class LowerThan(ABC[SupportsLt[T]], Generic[T]):
    def __init__(self, exclusive_maximum: T, /):
        self.exclusive_maximum = exclusive_maximum

    def check(self, value: SupportsLt[T], /) -> bool:
        return value < self.exclusive_maximum

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.exclusive_maximum!r})"


class LowerEquals(ABC[SupportsLe[T]], Generic[T]):
    def __init__(self, maximum: T, /):
        self.maximum = maximum

    def check(self, value: SupportsLe[T], /) -> bool:
        return value <= self.maximum

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.maximum!r})"


class GreaterThan(ABC[SupportsGt[T]], Generic[T]):
    def __init__(self, exclusive_minimum: T, /):
        self.exclusive_minimum = exclusive_minimum

    def check(self, value: SupportsGt[T], /) -> bool:
        return value > self.exclusive_minimum

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.exclusive_minimum!r})"


class GreaterEquals(ABC[SupportsGe[T]], Generic[T]):
    def __init__(self, minimum: T, /):
        self.minimum = minimum

    def check(self, value: SupportsGe[T], /) -> bool:
        return value >= self.minimum

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.minimum!r})"


class Range(ABC[object]):
    def __init__(self, min: int, max: int, step: int | None = None):
        self.min = min
        self.max = max
        self.step = step if step is not None else 1

    def check(self, value: object, /) -> bool:
        return value in range(self.min, self.max + 1, self.step)

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.min}, {self.max}, {self.step})"


class Contains(ABC[Container[T]], Generic[T]):
    def __init__(self, item: T, /):
        self.item = item

    def check(self, value: Container[T], /) -> bool:
        return self.item in value

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.item!r})"


class In(ABC[T], Generic[T]):
    def __init__(self, container: Container[T], /):
        self.container = container

    def check(self, value: T, /) -> bool:
        return value in self.container

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.container!r})"


class Pattern(ABC[str]):
    def __init__(self, pattern: regex.Pattern[str], /):
        self.pattern = pattern

    def check(self, value: str, /) -> bool:
        return bool(self.pattern.fullmatch(value))


positive = GreaterThan(0)

negative = LowerThan(0)

non_positive = LowerEquals(0)

non_negative = GreaterEquals(0)


def convert(callable: Callable[[T], bool], /) -> FromCallable[T]:
    return FromCallable(callable)


@convert
def truthy(_: object, /) -> bool:
    return True


@convert
def falsy(_: object, /) -> bool:
    return False
