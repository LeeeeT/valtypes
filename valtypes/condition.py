from __future__ import annotations

import abc
import re
from collections.abc import Callable, Container
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from .typing import GenericAlias, SupportsGe, SupportsGt, SupportsLe, SupportsLt, UnionType
from .util import resolve_type_args

__all__ = [
    "ABC",
    "And",
    "Contains",
    "Decorated",
    "Equals",
    "GenericAliasOf",
    "GreaterEquals",
    "GreaterThan",
    "In",
    "Is",
    "IsInstance",
    "IsSubclass",
    "LessEquals",
    "LessThan",
    "Not",
    "Or",
    "Pattern",
    "StrictGenericAliasOf",
    "false",
    "is_fixed_length_tuple",
    "is_variable_length_tuple",
    "true",
]

T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)

F = TypeVar("F")


class ABC(abc.ABC, Generic[T_contra]):
    @abc.abstractmethod
    def __call__(self, value: T_contra, /) -> bool:
        pass

    def __and__(self, other: Callable[[Any], bool], /) -> And[T_contra]:
        return And((self, other))

    def __rand__(self: ABC[Any], other: Callable[[T], bool], /) -> And[T]:
        return And((other, self))

    def __or__(self: ABC[T], other: Callable[[T], bool], /) -> Or[T]:
        return Or((self, other))

    def __ror__(self: ABC[T], other: Callable[[T], bool], /) -> Or[T]:
        return Or((other, self))

    def __invert__(self) -> Not[T_contra]:
        return Not(self)

    def __rrshift__(self, other: Callable[[T], T_contra], /) -> ABC[T]:
        return Decorated(other, self)


@dataclass
class And(ABC[T], Generic[T]):
    conditions: tuple[Callable[[T], bool], ...]

    def __call__(self, value: T, /) -> bool:
        return all(condition(value) for condition in self.conditions)


@dataclass
class Or(ABC[T], Generic[T]):
    conditions: tuple[Callable[[T], bool], ...]

    def __call__(self, value: T, /) -> bool:
        return any(condition(value) for condition in self.conditions)


@dataclass
class Not(ABC[T], Generic[T]):
    condition: Callable[[T], bool]

    def __call__(self, value: T, /) -> bool:
        return not self.condition(value)


class Decorated(ABC[T], Generic[T]):
    def __init__(self, decorator: Callable[[T], F], condition: Callable[[F], bool]):
        self.decorator = decorator
        self.condition = condition

    def __call__(self, value: T, /) -> bool:
        return self.condition(self.decorator(value))


@dataclass
class Wrap(ABC[T], Generic[T]):
    condition: Callable[[T], bool]

    def __call__(self, value: T, /) -> bool:
        return self.condition(value)


@dataclass
class Is(ABC[object]):
    object: object

    def __call__(self, value: object, /) -> bool:
        return value is self.object


@dataclass
class IsInstance(ABC[object]):
    type: type | UnionType

    def __call__(self, value: object, /) -> bool:
        try:
            return isinstance(value, self.type)
        except TypeError:
            return False


@dataclass
class IsSubclass(ABC[object]):
    type: type | UnionType

    def __call__(self, value: object, /) -> bool:
        return isinstance(value, type) and issubclass(value, self.type)


@dataclass
class Equals(ABC[object]):
    object: object

    def __call__(self, value: object, /) -> bool:
        return value == self.object


@dataclass
class LessThan(ABC[SupportsLt[T]], Generic[T]):
    exclusive_maximum: T

    def __call__(self, value: SupportsLt[T], /) -> bool:
        return value < self.exclusive_maximum


@dataclass
class LessEquals(ABC[SupportsLe[T]], Generic[T]):
    maximum: T

    def __call__(self, value: SupportsLe[T], /) -> bool:
        return value <= self.maximum


@dataclass
class GreaterThan(ABC[SupportsGt[T]], Generic[T]):
    exclusive_minimum: T

    def __call__(self, value: SupportsGt[T], /) -> bool:
        return value > self.exclusive_minimum


@dataclass
class GreaterEquals(ABC[SupportsGe[T]], Generic[T]):
    minimum: T

    def __call__(self, value: SupportsGe[T], /) -> bool:
        return value >= self.minimum


@dataclass
class Contains(ABC[Container[T]], Generic[T]):
    item: T

    def __call__(self, value: Container[T], /) -> bool:
        return self.item in value


@dataclass
class In(ABC[T], Generic[T]):
    container: Container[T]

    def __call__(self, value: T, /) -> bool:
        return value in self.container


@dataclass
class Pattern(ABC[str]):
    pattern: re.Pattern[str]

    def __call__(self, value: str, /) -> bool:
        return bool(self.pattern.match(value))


@dataclass
class GenericAliasOf(ABC[object]):
    type: type

    def __call__(self, value: object, /) -> bool:
        if not isinstance(value, GenericAlias):
            return False
        try:
            return issubclass(value.__origin__, self.type)
        except TypeError:
            return False


@dataclass
class StrictGenericAliasOf(ABC[object]):
    type: type

    def __call__(self, value: object, /) -> bool:
        return isinstance(value, GenericAlias) and value.__origin__ is self.type


@Wrap
def true(value: object, /) -> bool:
    return True


@Wrap
def false(value: object, /) -> bool:
    return False


@Wrap
def is_fixed_length_tuple(value: object, /) -> bool:
    if not isinstance(value, GenericAlias):
        return False
    if value.__origin__ is not tuple:
        return False
    if len(resolve_type_args(value, tuple)) == 2 and resolve_type_args(value, tuple)[1] == ...:
        return False
    return True


@Wrap
def is_variable_length_tuple(value: object, /) -> bool:
    if not isinstance(value, GenericAlias):
        return False
    if value.__origin__ is not tuple:
        return False
    return len(resolve_type_args(value, tuple)) == 2 and resolve_type_args(value, tuple)[1] == ...
