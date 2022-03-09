from typing import Generic, Protocol, TypeGuard, TypeVar, Union
from typing import _UnionGenericAlias as UnionGenericAlias  # type: ignore

from valtypes.typing import GenericAlias, HasOrigBases

__all__ = ["resolve_type_args"]


class TypeArgsResolver:
    def __init__(self, target_class: type):
        self._target_class = target_class

    def resolve(self, source_type: type | GenericAlias) -> tuple[object, ...]:
        if self._is_generic(source_type):
            return self._resolve_generic(source_type)
        if self._has_orig_bases(source_type):
            return self._resolve_subclass_of_generic(source_type)
        return self._resolve_class(source_type)

    @staticmethod
    def _is_generic(typ: type | GenericAlias) -> bool:
        return isinstance(typ, GenericAlias) or typ is not Protocol and Generic in typ.__bases__  # type: ignore

    def _resolve_generic(self, generic: type | GenericAlias) -> tuple[object, ...]:
        alias = self._restore_missing_type_args(generic)
        if alias.__origin__ is self._target_class:
            return alias.__args__  # type: ignore
        elif Generic in alias.__origin__.__bases__:
            return self._search_in_bases(self._propagate_type_args_to_bases(alias))
        return ()

    def _restore_missing_type_args(self, alias: type | GenericAlias) -> GenericAlias:
        missing_type_args = tuple(
            self._get_type_var_bound(type_var) for type_var in alias.__parameters__  # type: ignore
        )
        return alias[missing_type_args] if missing_type_args else alias  # type: ignore

    @staticmethod
    def _get_type_var_bound(type_var: TypeVar) -> object:
        if type_var.__constraints__:
            return UnionGenericAlias(Union, type_var.__constraints__)
        return object if type_var.__bound__ is None else type_var.__bound__

    def _propagate_type_args_to_bases(self, alias: GenericAlias) -> tuple[type | GenericAlias, ...]:
        return tuple(
            self._propagate_type_args_to_alias(alias, base) if isinstance(base, GenericAlias) else base
            for base in self._get_alias_bases(alias)
        )

    def _propagate_type_args_to_alias(self, from_alias: GenericAlias, to_alias: GenericAlias) -> GenericAlias:
        vars_to_args = self._create_vars_to_args_mapping(from_alias)
        args = tuple(vars_to_args[var] for var in to_alias.__parameters__)
        return to_alias[args]

    def _create_vars_to_args_mapping(self, alias: GenericAlias) -> dict[TypeVar, object]:
        return dict(zip(self._get_generic_base(alias.__origin__).__parameters__, alias.__args__))

    @staticmethod
    def _get_generic_base(generic: GenericAlias) -> GenericAlias:
        for base in generic.__orig_bases__:
            if isinstance(base, GenericAlias) and base.__origin__ is Generic:
                return base
        raise TypeError(f"{Generic} is not in {generic} bases")

    @staticmethod
    def _get_alias_bases(alias: GenericAlias) -> tuple[type | GenericAlias, ...]:
        return tuple(
            base
            for base in alias.__origin__.__orig_bases__
            if not (isinstance(base, GenericAlias) and base.__origin__ is Generic)
        )

    def _search_in_bases(self, bases: tuple[type | GenericAlias, ...]) -> tuple[object, ...]:
        for base in bases:
            if type_args := self.resolve(base):
                return type_args
        return ()

    @staticmethod
    def _has_orig_bases(obj: object) -> TypeGuard[HasOrigBases]:
        return hasattr(obj, "__orig_bases__")

    def _resolve_subclass_of_generic(self, cls: HasOrigBases) -> tuple[object, ...]:
        return self._search_in_bases(cls.__orig_bases__)

    def _resolve_class(self, cls: type) -> tuple[object, ...]:
        return self._search_in_bases(cls.__bases__)


def resolve_type_args(source_type: type | GenericAlias, target_class: type) -> tuple[object, ...]:
    return TypeArgsResolver(target_class).resolve(source_type)
