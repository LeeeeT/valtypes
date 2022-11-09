from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from valtypes import error
from valtypes.collection import Collection
from valtypes.parsing import parser
from valtypes.util import cached_method

if TYPE_CHECKING:
    from valtypes.parsing import rule

from .abc import ABC

__all__ = ["Composite"]


T = TypeVar("T")

F = TypeVar("F")


class Composite(ABC[object, T, F], Collection["rule.ABC[T, F]"], Generic[T, F]):
    @cached_method
    def get_parser_for(self, type: object, /) -> parser.ABC[T, F]:  # type: ignore
        for rule in self:
            if rule.is_suitable_for(type):
                return rule.get_parser_for(type)
        raise error.NoParser(type)

    def add_to_top(self, *rules: rule.ABC[T, F]) -> None:
        self.get_parser_for.cache_clear()
        super().add_to_top(*rules)
