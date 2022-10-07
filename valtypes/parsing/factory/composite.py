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


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class Composite(ABC[object, T_contra, T_co], Collection["rule.ABC[T_contra, T_co]"], Generic[T_contra, T_co]):
    @cached_method
    def get_parser_for(self, type: object, /) -> parser.ABC[T_contra, T_co]:  # type: ignore
        for rule in self:
            if rule.is_suitable_for(type):
                return rule.get_parser_for(type)
        raise error.NoParser(type)

    def add_to_top(self, *rules: rule.ABC[T_contra, T_co]) -> None:
        self.get_parser_for.cache_clear()
        super().add_to_top(*rules)
