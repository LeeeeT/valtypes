from collections.abc import Iterator
from types import UnionType
from typing import Any, Generic, TypeVarTuple
from typing import _GenericAlias as GenericAlias  # type: ignore

from valtypes.typing import GenericAlias as GenericAliasType

__all__ = ["resolve_type_arguments"]


class TypeArgumentsResolver:
    def __init__(self, type: Any, target: type):
        self._type = type
        self._target = target

    def resolve(self) -> Any:
        if isinstance(self._type, GenericAliasType) and self._origin is self._target:
            return self._type
        return resolve_type_arguments(self._intermediate_target, self._target)

    @property
    def _intermediate_target(self) -> Any:
        if isinstance(self._type, GenericAliasType):
            return self._parameterized_bases_union.__args__[self._intermediate_target_index_in_bases]
        return tuple(self._parameterized_bases)[self._intermediate_target_index_in_bases]

    @property
    def _parameterized_bases_union(self) -> UnionType:
        if issubclass(self._origin, Generic):
            return self._parameterized_bases_union_of_generic
        return self._parameterized_bases_union_of_non_generic

    @property
    def _parameterized_bases_union_of_generic(self) -> UnionType:
        return GenericAlias(object, (self._origin[*self._original_parameters], self._bases_union))[*self._original_arguments].__args__[1]

    @property
    def _parameterized_bases_union_of_non_generic(self) -> UnionType:
        return self._bases_union[*self._original_arguments]

    @property
    def _original_parameters(self) -> Iterator[Any]:
        return get_parameters(self._origin)

    @property
    def _original_arguments(self) -> tuple[Any, ...]:
        return self._type.__args__

    @property
    def _bases_union(self) -> Any:
        return GenericAlias(object, tuple(self._parameterized_bases))

    @property
    def _origin(self) -> Any:
        return self._type.__origin__

    @property
    def _intermediate_target_index_in_bases(self) -> int:
        return next(index for index, base in enumerate(self._parameterized_bases_origins) if issubclass(base, self._target))  # pragma: no cover

    @property
    def _parameterized_bases_origins(self) -> Iterator[Any]:
        return (base.__origin__ if isinstance(base, GenericAliasType) else base for base in self._parameterized_bases)  # pragma: no cover

    @property
    def _parameterized_bases(self) -> Iterator[Any]:
        if isinstance(self._type, GenericAliasType):
            return self._orig_bases_of_generic_alias
        return getattr(self._type, "__orig_bases__", self._bases_of_class)  # type: ignore

    @property
    def _orig_bases_of_generic_alias(self) -> Iterator[Any]:
        for base in self._origin.__orig_bases__:
            if not isinstance(base, GenericAliasType) or base.__origin__ is not Generic:
                yield base

    @property
    def _bases_of_class(self) -> tuple[Any, ...]:
        return self._type.__bases__


def get_parameters(type: Any) -> Iterator[Any]:
    for parameter in type.__parameters__:
        if isinstance(parameter, TypeVarTuple):
            yield from parameter
        else:
            yield parameter


def resolve_type_arguments(type: Any, target: type) -> Any:
    return TypeArgumentsResolver(type, target).resolve()
