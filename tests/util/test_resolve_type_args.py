from typing import Generic, ParamSpec, TypeVar, TypeVarTuple

from valtypes.util import resolve_type_arguments

T = TypeVar("T")

F = TypeVar("F")

Ts = TypeVarTuple("Ts")

P = ParamSpec("P")


class Base:
    pass


class ParameterizedList(list[int]):
    pass


class SubclassOfParameterizedList(Base, ParameterizedList):
    pass


class NonParameterizedList(Base, list[T]):
    pass


class NonParameterizedListRedundantGeneric(Base, list[F], Generic[F]):
    pass


class GenericClass1(Generic[T, P]):
    pass


class GenericClass2(Generic[T]):
    pass


class ParameterizedGenericClass(GenericClass2[int], GenericClass1[bytes, [str]]):
    pass


class SubclassOfParameterizedGenericClass(Base, ParameterizedGenericClass):
    pass


class NonParameterizedGenericClass(Base, GenericClass1[T, P]):
    pass


class NonParameterizedGenericClassRedundantGeneric(Base, GenericClass1[F, P], Generic[F, P]):
    pass


class PartiallyParameterizedGenericClass(Base, GenericClass1[T, [int]]):
    pass


class PartiallyParameterizedGenericClassRedundantGeneric(Base, GenericClass1[F, [F]], Generic[F]):
    pass


class VariadicGeneric(Base, tuple[*Ts], Generic[T, *Ts, F]):
    pass


def test_returns_alias_unchanged_if_origin_matches_target() -> None:
    assert resolve_type_arguments(list[int], list) == list[int]
    assert resolve_type_arguments(tuple[int, *tuple[None, ...]], tuple) == tuple[int, *tuple[None, ...]]


def test_finds_target_in_bases() -> None:
    assert resolve_type_arguments(ParameterizedList, list) == list[int]
    assert resolve_type_arguments(ParameterizedGenericClass, GenericClass1) == GenericClass1[bytes, [str]]

    assert resolve_type_arguments(SubclassOfParameterizedList, list) == list[int]
    assert resolve_type_arguments(SubclassOfParameterizedGenericClass, GenericClass1) == GenericClass1[bytes, [str]]


def test_propagates_type_args_to_bases() -> None:
    assert resolve_type_arguments(NonParameterizedList[float], list) == list[float]
    assert resolve_type_arguments(NonParameterizedGenericClass[float, [int]], GenericClass1) == GenericClass1[float, [int]]

    assert resolve_type_arguments(NonParameterizedListRedundantGeneric[float], list) == list[float]
    assert resolve_type_arguments(NonParameterizedGenericClassRedundantGeneric[float, [int]], GenericClass1) == GenericClass1[float, [int]]

    assert resolve_type_arguments(PartiallyParameterizedGenericClass[float], GenericClass1) == GenericClass1[float, [int]]

    # uncomment when python/cpython#88965 is fixed
    # assert resolve_type_args(PartiallyParameterizedGenericClassRedundantGeneric[float], GenericClass1) == GenericClass1[float, [float]]


def test_properly_assigns_type_var_tuple() -> None:
    assert resolve_type_arguments(VariadicGeneric[int, str, bytes, float], tuple) == tuple[str, bytes]
