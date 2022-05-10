from collections.abc import Iterable

from valtypes.typing import GenericAlias

__all__ = ["TypeArgsResolver", "resolve_type_args"]


class TypeArgsResolver:
    def __init__(self, target_class: type):
        self._target_class = target_class

    def resolve(self, origin: type | GenericAlias) -> tuple[object, ...]:
        if isinstance(origin, GenericAlias):
            return self._search_in_alias(origin)
        return self._search_in_class(origin)

    def _search_in_class(self, cls: type) -> tuple[object, ...]:
        if cls is self._target_class:
            raise TypeError(f"{self._target_class} is not a generic")
        return self._search_in_bases(cls)

    def _search_in_alias(self, alias: GenericAlias) -> tuple[object, ...]:
        if alias.__origin__ is self._target_class:
            return alias.__args__  # type: ignore
        return self._search_in_bases(alias)

    def _search_in_bases(self, origin: type | GenericAlias) -> tuple[object, ...]:
        for base in self._get_bases(origin):
            try:
                return self.resolve(base)
            except TypeError:
                pass
        raise TypeError(f"{self._target_class} is not found in {origin} bases")

    def _get_bases(self, origin: type | GenericAlias) -> Iterable[type | GenericAlias]:
        if isinstance(origin, GenericAlias):
            return (self._propagate_type_args(origin, base) if isinstance(base, GenericAlias) else base for base in self._get_bases(origin.__origin__))
        return getattr(origin, "__orig_bases__", origin.__bases__)

    @staticmethod
    def _propagate_type_args(from_alias: GenericAlias, to_alias: GenericAlias) -> GenericAlias:
        var_to_arg = dict(zip(from_alias.__origin__.__parameters__, from_alias.__args__))
        return to_alias[tuple(var_to_arg[type_var] for type_var in to_alias.__parameters__)]


def resolve_type_args(origin: type | GenericAlias, target_class: type) -> GenericAlias:
    return TypeArgsResolver(target_class).resolve(origin)
