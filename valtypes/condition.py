from __future__ import annotations

import abc
import re
from collections.abc import Callable, Container
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
        return And(self, other)

    def __rand__(self: ABC[Any], other: Callable[[T], bool], /) -> And[T]:
        return And(other, self)

    def __or__(self: ABC[T], other: Callable[[T], bool], /) -> Or[T]:
        return Or(self, other)

    def __ror__(self: ABC[T], other: Callable[[T], bool], /) -> Or[T]:
        return Or(other, self)

    def __invert__(self) -> Not[T_contra]:
        return Not(self)

    def __rrshift__(self, other: Callable[[T], T_contra], /) -> ABC[T]:
        return Decorated(other, self)


class And(ABC[T], Generic[T]):
    def __init__(self, *conditions: Callable[[T], bool]):
        self.conditions = conditions

    def __call__(self, value: T, /) -> bool:
        return all(condition(value) for condition in self.conditions)


class Or(ABC[T], Generic[T]):
    def __init__(self, *conditions: Callable[[T], bool]):
        self.conditions = conditions

    def __call__(self, value: T, /) -> bool:
        return any(condition(value) for condition in self.conditions)


class Not(ABC[T], Generic[T]):
    def __init__(self, condition: Callable[[T], bool], /):
        self.condition = condition

    def __call__(self, value: T, /) -> bool:
        return not self.condition(value)


class Decorated(ABC[T], Generic[T]):
    def __init__(self, decorator: Callable[[T], F], condition: Callable[[F], bool]):
        self.decorator = decorator
        self.condition = condition

    def __call__(self, value: T, /) -> bool:
        return self.condition(self.decorator(value))


class Wrap(ABC[T], Generic[T]):
    def __init__(self, condition: Callable[[T], bool], /):
        self.condition = condition

    def __call__(self, value: T, /) -> bool:
        return self.condition(value)


class Is(ABC[object]):
    def __init__(self, object: object, /):
        self.object = object

    def __call__(self, value: object, /) -> bool:
        return value is self.object


class IsInstance(ABC[object]):
    def __init__(self, type: type | UnionType, /):
        self.type = type

    def __call__(self, value: object, /) -> bool:
        try:
            return isinstance(value, self.type)
        except TypeError:
            return False


class IsSubclass(ABC[object]):
    def __init__(self, type: type | UnionType, /):
        self.type = type

    def __call__(self, value: object, /) -> bool:
        return isinstance(value, type) and issubclass(value, self.type)


class Equals(ABC[object]):
    def __init__(self, obj: object, /):
        self.object = obj

    def __call__(self, value: object, /) -> bool:
        return value == self.object


class LessThan(ABC[SupportsLt[T]], Generic[T]):
    def __init__(self, exclusive_maximum: T, /):
        self.exclusive_maximum = exclusive_maximum

    def __call__(self, value: SupportsLt[T], /) -> bool:
        return value < self.exclusive_maximum


class LessEquals(ABC[SupportsLe[T]], Generic[T]):
    def __init__(self, maximum: T, /):
        self.maximum = maximum

    def __call__(self, value: SupportsLe[T], /) -> bool:
        return value <= self.maximum


class GreaterThan(ABC[SupportsGt[T]], Generic[T]):
    def __init__(self, exclusive_minimum: T, /):
        self.exclusive_minimum = exclusive_minimum

    def __call__(self, value: SupportsGt[T], /) -> bool:
        return value > self.exclusive_minimum


class GreaterEquals(ABC[SupportsGe[T]], Generic[T]):
    def __init__(self, minimum: T, /):
        self.minimum = minimum

    def __call__(self, value: SupportsGe[T], /) -> bool:
        return value >= self.minimum


class Contains(ABC[Container[T]], Generic[T]):
    def __init__(self, item: T, /):
        self.item = item

    def __call__(self, value: Container[T], /) -> bool:
        return self.item in value


class In(ABC[T], Generic[T]):
    def __init__(self, container: Container[T], /):
        self.container = container

    def __call__(self, value: T, /) -> bool:
        return value in self.container


class Pattern(ABC[str]):
    def __init__(self, pattern: re.Pattern[str], /):
        self.pattern = pattern

    def __call__(self, value: str, /) -> bool:
        return bool(self.pattern.match(value))


class GenericAliasOf(ABC[object]):
    def __init__(self, type: type, /):
        self.type = type

    def __call__(self, value: object, /) -> bool:
        if not isinstance(value, GenericAlias):
            return False
        try:
            return issubclass(value.__origin__, self.type)
        except TypeError:
            return False


class StrictGenericAliasOf(ABC[object]):
    def __init__(self, type: type, /):
        self.type = type

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
