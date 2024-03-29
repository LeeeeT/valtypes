from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, TypeVar

from valtypes import error
from valtypes.collection import Collection
from valtypes.parsing import parser

if TYPE_CHECKING:
    from valtypes.parsing import rule

from .abc import ABC

__all__ = ["Composite"]


T = TypeVar("T")

F = TypeVar("F")


class Composite(ABC[object, T, F], Collection["rule.ABC[T, F]"]):
    def get_parser_for(self, type: object, /) -> parser.ABC[T, F]:
        if type not in self._cache:
            self._cache[type] = self._find_parser_for(type)
        return self._cache[type]

    def _find_parser_for(self, type: object, /) -> parser.ABC[T, F]:
        for rule in self:
            if rule.is_suitable_for(type):
                return rule.get_parser_for(type)
        raise error.NoParser(type)

    def add_to_top(self, *rules: rule.ABC[T, F]) -> None:
        self._cache.clear()
        super().add_to_top(*rules)

    @cached_property
    def _cache(self) -> dict[object, parser.ABC[T, F]]:
        return {}
