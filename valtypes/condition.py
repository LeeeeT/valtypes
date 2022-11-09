from __future__ import annotations

import abc
from collections.abc import Callable
from dataclasses import InitVar, dataclass, is_dataclass
from types import UnionType
from typing import Any, Generic, TypeVar

from valtypes.typing import Dataclass, GenericAlias, LiteralAlias, UnionAlias
from valtypes.util import resolve_type_arguments

from . import decorator

__all__ = [
    "ABC",
    "AliasOf",
    "And",
    "Decorated",
    "FromCallable",
    "InstanceOf",
    "Is",
    "Not",
    "ObjectIsAliasOf",
    "ObjectIsStrictAliasOf",
    "ObjectIsStrictSubclassOf",
    "ObjectIsSubclassOf",
    "Or",
    "Shortcut",
    "Shortcut",
    "StrictAliasOf",
    "SubclassOf",
    "builtin_type",
    "dataclass_with_init",
    "fixed_length_tuple_alias",
    "generic_alias",
    "init_var",
    "object_is_alias_of_list",
    "object_is_fixed_length_tuple_alias",
    "object_is_strict_alias_of_list",
    "object_is_strict_subclass_of_bytearray",
    "object_is_strict_subclass_of_bytes",
    "object_is_strict_subclass_of_float",
    "object_is_strict_subclass_of_int",
    "object_is_strict_subclass_of_str",
    "object_is_tuple_alias",
    "object_is_variable_length_tuple_alias",
    "union_alias",
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


@dataclass(init=False, repr=False)
class And(ABC[T_contra]):
    _first: ABC[T_contra]
    _second: ABC[Any]

    def __init__(self, first: ABC[T_contra], second: ABC[Any]):
        self._first = first
        self._second = second

    def check(self, value: T_contra, /) -> bool:
        return self._first.check(value) and self._second.check(value)


@dataclass(init=False, repr=False)
class Or(ABC[T_contra]):
    _first: ABC[T_contra]
    _second: ABC[Any]

    def __init__(self, first: ABC[T_contra], second: ABC[Any]):
        self._first = first
        self._second = second

    def check(self, value: T_contra, /) -> bool:
        return self._first.check(value) or self._second.check(value)


@dataclass(init=False, repr=False)
class Decorated(ABC[T_contra]):
    _decorator: decorator.ABC[T_contra, Any]
    _condition: ABC[Any]

    def __init__(self, decorator: decorator.ABC[T_contra, T], condition: ABC[T]):
        self._decorator = decorator
        self._condition = condition

    def check(self, value: T_contra, /) -> bool:
        return self._condition.check(self._decorator.decorate(value))


@dataclass(init=False, repr=False)
class Not(ABC[T_contra]):
    _condition: ABC[T_contra]

    def __init__(self, condition: ABC[T_contra]):
        self._condition = condition

    def check(self, value: T_contra, /) -> bool:
        return not self._condition.check(value)


@dataclass(init=False, repr=False)
class Shortcut(ABC[T_contra]):
    _condition: ABC[T_contra]

    def __init__(self, condition: ABC[T_contra]):
        self._condition = condition

    def check(self, value: T_contra, /) -> bool:
        return self._condition.check(value)


@dataclass(init=False, repr=False)
class FromCallable(ABC[T_contra]):
    _callable: Callable[[T_contra], bool]

    def __init__(self, callable: Callable[[T_contra], bool]):
        self._callable = callable

    def check(self, value: T_contra, /) -> bool:
        return self._callable(value)


@dataclass(init=False, repr=False)
class InstanceOf(ABC[object]):
    _type: type | UnionType

    def __init__(self, type: type | UnionType):
        self._type = type

    def check(self, value: object, /) -> bool:
        return isinstance(value, self._type)


@dataclass(init=False, repr=False)
class Is(ABC[object]):
    _object: object

    def __init__(self, object: object):
        self._object = object

    def check(self, value: object, /) -> bool:
        return value is self._object


@dataclass(init=False, repr=False)
class SubclassOf(ABC[type]):
    _type: type | UnionType

    def __init__(self, type: type | UnionType):
        self._type = type

    def check(self, value: type, /) -> bool:
        return issubclass(value, self._type)


class ObjectIsSubclassOf(Shortcut[object]):
    def __init__(self, type: type | UnionType):
        super().__init__(is_class & SubclassOf(type))


class ObjectIsStrictSubclassOf(Shortcut[object]):
    def __init__(self, type: type):
        super().__init__(~Is(type) & ObjectIsSubclassOf(type))


class AliasOf(Shortcut[GenericAlias]):
    def __init__(self, type: type):
        super().__init__(decorator.origin >> ObjectIsSubclassOf(type))


class ObjectIsAliasOf(Shortcut[object]):
    def __init__(self, type: type):
        super().__init__(generic_alias & AliasOf(type))


class StrictAliasOf(Shortcut[GenericAlias]):
    def __init__(self, type: type):
        super().__init__(decorator.origin >> Is(type))


class ObjectIsStrictAliasOf(Shortcut[object]):
    def __init__(self, type: type):
        super().__init__(generic_alias & StrictAliasOf(type))


generic_alias: InstanceOf = InstanceOf(GenericAlias)
union_alias: InstanceOf = InstanceOf(UnionAlias)
literal_alias: InstanceOf = InstanceOf(LiteralAlias)


is_class: And[object] = InstanceOf(type) & ~generic_alias


builtin_type: Or[object] = Is(int) | Is(float) | Is(str) | Is(bytes) | Is(bytearray) | Is(object)


@FromCallable
def variable_length_tuple_alias(value: GenericAlias, /) -> bool:
    match resolve_type_arguments(value, tuple).__args__:
        case (_, second_argument) if second_argument is ...:
            return True
        case _:
            return False


fixed_length_tuple_alias: Not[GenericAlias] = ~variable_length_tuple_alias

object_is_tuple_alias: ObjectIsAliasOf = ObjectIsAliasOf(tuple)
object_is_variable_length_tuple_alias: And[object] = object_is_tuple_alias & variable_length_tuple_alias
object_is_fixed_length_tuple_alias: And[object] = object_is_tuple_alias & fixed_length_tuple_alias


@FromCallable
def dataclass_with_init(value: Dataclass, /) -> bool:
    return is_class.check(value) and is_dataclass(value) and value.__dataclass_params__.init


init_var: InstanceOf = InstanceOf(InitVar)


object_is_strict_subclass_of_int: ObjectIsStrictSubclassOf = ObjectIsStrictSubclassOf(int)
object_is_strict_subclass_of_float: ObjectIsStrictSubclassOf = ObjectIsStrictSubclassOf(float)
object_is_strict_subclass_of_str: ObjectIsStrictSubclassOf = ObjectIsStrictSubclassOf(str)
object_is_strict_subclass_of_bytes: ObjectIsStrictSubclassOf = ObjectIsStrictSubclassOf(bytes)
object_is_strict_subclass_of_bytearray: ObjectIsStrictSubclassOf = ObjectIsStrictSubclassOf(bytearray)


object_is_alias_of_list: ObjectIsAliasOf = ObjectIsAliasOf(list)
object_is_strict_alias_of_list: ObjectIsStrictAliasOf = ObjectIsStrictAliasOf(list)
