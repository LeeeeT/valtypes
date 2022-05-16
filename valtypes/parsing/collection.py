from collections.abc import Callable
from functools import lru_cache
from typing import Any, TypeVar, overload

from valtypes import collection

from .controller import Controller
from .rule import Rule

__all__ = ["Collection"]


T = TypeVar("T")

T_Parser = TypeVar("T_Parser", bound=Callable[[Any, Any, Controller], Any])


class Collection(collection.Collection[Rule]):
    def add(self, *rules: Rule) -> None:
        super().add(*rules)
        self.get_parsers_matching_type.cache_clear()

    @overload
    def parse(self, target_type: type[T], source: object) -> T:
        ...

    @overload
    def parse(self, target_type: Any, source: object) -> Any:
        ...

    def parse(self, target_type: object, source: object) -> Any:
        return Controller(self).delegate(target_type, source)

    def register(self, target_condition: Callable[[object], bool]) -> Callable[[T_Parser], T_Parser]:
        def registrar(parser: T_Parser) -> T_Parser:
            self.add(Rule(parser, target_condition))
            return parser

        return registrar

    @lru_cache(1024)
    def get_parsers_matching_type(self, type: object, /) -> list[Callable[[Any, Any, Controller], Any]]:
        return [rule.parser for rule in self if rule.target_condition(type)]
