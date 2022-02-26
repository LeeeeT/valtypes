from collections.abc import Mapping
from typing import Generic, TypeVar

from valtypes.typing import GenericAlias

__all__ = ["resolve_type_args"]


class TypeArgsResolver:
    _generic_alias: GenericAlias
    _target_class: type
    _resolved_type_args: tuple[object, ...] | None

    _generic: type[Generic]  # type: ignore
    _base_generic_class: type[Generic]  # type: ignore

    _generic_alias_bases: list[GenericAlias]

    _type_vars: tuple[TypeVar, ...]
    _type_args: tuple[object, ...]
    _type_vars_to_type_args: Mapping[TypeVar, object]

    def resolve(self, generic_alias: GenericAlias, target_class: type) -> tuple[object, ...]:
        self._generic_alias = generic_alias
        self._target_class = target_class

        self._try_resolve()

        if self._resolved_type_args is None:
            raise TypeError(f"{target_class} is not in {generic_alias} bases")

        return self._resolved_type_args

    def _try_resolve(self) -> None:
        if issubclass(self._generic_alias, Generic):  # type: ignore
            self._generic = self._generic_alias
            self._resolve_generic()
        elif self._generic_alias.__origin__ is self._target_class:
            self._resolved_type_args = self._generic_alias.__args__
        else:
            self._resolved_type_args = None

    def _resolve_generic(self) -> None:
        self._get_generic_alias_bases()
        self._extract_base_generic_class()
        self._create_type_vars_to_type_args_mapping()
        self._resolve_generic_alias_bases()

    def _get_generic_alias_bases(self) -> None:
        self._generic_alias_bases = [
            base for base in self._generic.__orig_bases__ if isinstance(base, GenericAlias)  # type: ignore
        ]

    def _extract_base_generic_class(self) -> None:
        for i, base in enumerate(self._generic_alias_bases):
            if base.__origin__ is Generic:
                self._base_generic_class = self._generic_alias_bases.pop(i)

    def _create_type_vars_to_type_args_mapping(self) -> None:
        self._get_type_vars()
        self._get_type_args()
        self._type_vars_to_type_args = dict(zip(self._type_vars, self._type_args))

    def _get_type_vars(self) -> None:
        self._type_vars = self._base_generic_class.__args__  # type: ignore

    def _get_type_args(self) -> None:
        self._type_args = self._generic.__args__ + (object,) * (  # type: ignore
            len(self._type_vars) - len(self._generic.__args__)  # type: ignore
        )

    def _resolve_generic_alias_bases(self) -> None:
        for base in self._generic_alias_bases:
            missing_type_args = tuple(self._type_vars_to_type_args[type_var] for type_var in base.__parameters__)
            new_type = base.__class_getitem__(missing_type_args)
            try:
                self._resolved_type_args = self.__class__().resolve(new_type, self._target_class)
            except TypeError:
                pass


def resolve_type_args(generic_alias: GenericAlias, target_class: type) -> tuple[object, ...]:
    return TypeArgsResolver().resolve(generic_alias, target_class)
