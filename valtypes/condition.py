from __future__ import annotations

import abc
from collections.abc import Callable
from dataclasses import is_dataclass
from types import UnionType
from typing import Any, Generic, TypeVar, cast

from valtypes.typing import GenericAlias
from valtypes.util import resolve_type_args

from . import decorator

__all__ = [
    "ABC",
    "AliasOf",
    "And",
    "Decorated",
    "FromCallable",
    "InstanceOf",
    "Is",
    "LenientAliasOf",
    "LenientStrictAliasOf",
    "LenientStrictSubclassOf",
    "LenientSubclassOf",
    "Not",
    "Or",
    "Shortcut",
    "Shortcut",
    "StrictAliasOf",
    "SubclassOf",
    "dataclass_with_init",
    "fixed_length_tuple_alias",
    "generic_alias",
    "lenient_fixed_length_tuple_alias",
    "lenient_tuple_alias",
    "lenient_variable_length_tuple_alias",
    "variable_length_tuple_alias",
]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)


class ABC(abc.ABC, Generic[T_contra]):
    @abc.abstractmethod
    def check(self, value: T_contra, /) -> bool:
        pass

    def __and__(self, other: ABC[Any], /) -> And[T_contra]:
        if isinstance(other, ABC):
            return And(self, other)
        return NotImplemented

    def __or__(self, other: ABC[Any], /) -> Or[T_contra]:
        if isinstance(other, ABC):
            return Or(self, other)
        return NotImplemented

    def __rrshift__(self, other: decorator.ABC[T, T_contra], /) -> Decorated[T]:
        if isinstance(other, decorator.ABC):
            return Decorated(other, self)
        return NotImplemented

    def __invert__(self) -> Not[T_contra]:
        return Not(self)


class And(ABC[T_contra], Generic[T_contra]):
    def __init__(self, first: ABC[T_contra], second: ABC[Any]):
        self._first = first
        self._second = second

    def check(self, value: T_contra, /) -> bool:
        return self._first.check(value) and self._second.check(value)

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, And):
            return self._first == other._first and self._second == other._second
        return NotImplemented


class Or(ABC[T_contra], Generic[T_contra]):
    def __init__(self, first: ABC[T_contra], second: ABC[Any]):
        self._first = first
        self._second = second

    def check(self, value: T_contra, /) -> bool:
        return self._first.check(value) or self._second.check(value)

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, Or):
            return self._first == other._first and self._second == other._second
        return NotImplemented


class Decorated(ABC[T_contra]):
    def __init__(self, decorator: decorator.ABC[T_contra, T], condition: ABC[T]):
        self._decorator = decorator
        self._condition = condition

    def check(self, value: T_contra, /) -> bool:
        return self._condition.check(self._decorator.decorate(value))

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, Decorated):
            return self._decorator == other._decorator and self._condition == other._condition
        return NotImplemented


class Not(ABC[T_contra], Generic[T_contra]):
    def __init__(self, condition: ABC[T_contra]):
        self._condition = condition

    def check(self, value: T_contra, /) -> bool:
        return not self._condition.check(value)

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, Not):
            return self._condition == other._condition
        return NotImplemented


class Shortcut(ABC[T_contra], Generic[T_contra]):
    def __init__(self, condition: ABC[T_contra]):
        self._condition = condition

    def check(self, value: T_contra, /) -> bool:
        return self._condition.check(value)


class FromCallable(ABC[T_contra], Generic[T_contra]):
    def __init__(self, callable: Callable[[T_contra], bool]):
        self._callable = callable

    def check(self, value: T_contra, /) -> bool:
        return self._callable(value)


class InstanceOf(ABC[object]):
    def __init__(self, type: type | UnionType):
        self._type = type

    def check(self, value: object, /) -> bool:
        return isinstance(value, self._type)


class Is(ABC[object]):
    def __init__(self, object: object):
        self._object = object

    def check(self, value: object, /) -> bool:
        return value is self._object

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Is):
            return self._object == other._object
        return NotImplemented


class SubclassOf(ABC[type]):
    def __init__(self, type: type | UnionType):
        self._type = type

    def check(self, value: type, /) -> bool:
        return issubclass(value, self._type)


class LenientSubclassOf(Shortcut[object]):
    def __init__(self, type: type | UnionType):
        super().__init__(is_class & SubclassOf(type))


class LenientStrictSubclassOf(Shortcut[object]):
    def __init__(self, type: type):
        super().__init__(~Is(type) & LenientSubclassOf(type))


class AliasOf(Shortcut[GenericAlias]):
    def __init__(self, type: type):
        super().__init__(decorator.origin >> LenientSubclassOf(type))


class LenientAliasOf(Shortcut[object]):
    def __init__(self, type: type):
        super().__init__(generic_alias & AliasOf(type))


class StrictAliasOf(Shortcut[GenericAlias]):
    def __init__(self, type: type):
        super().__init__(decorator.origin >> Is(type))


class LenientStrictAliasOf(Shortcut[object]):
    def __init__(self, type: type):
        super().__init__(generic_alias & StrictAliasOf(type))


@FromCallable
def variable_length_tuple_alias(value: GenericAlias, /) -> bool:
    match resolve_type_args(value, tuple):
        case (_, second_argument) if second_argument is ...:
            return True
        case _:
            return False


@FromCallable
def dataclass_with_init(value: object, /) -> bool:
    return is_class.check(value) and is_dataclass(value) and cast(Any, value).__dataclass_params__.init


fixed_length_tuple_alias: Not[GenericAlias] = ~variable_length_tuple_alias


generic_alias: InstanceOf = InstanceOf(GenericAlias)


is_class: And[object] = InstanceOf(type) & ~generic_alias


lenient_tuple_alias: LenientAliasOf = LenientAliasOf(tuple)


lenient_variable_length_tuple_alias: And[object] = lenient_tuple_alias & variable_length_tuple_alias


lenient_fixed_length_tuple_alias: And[object] = lenient_tuple_alias & fixed_length_tuple_alias
