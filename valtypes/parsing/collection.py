from collections.abc import Callable
from functools import lru_cache
from typing import Any, TypeVar, overload

from .controller import Controller
from .rule import Rule

__all__ = ["Collection"]


T = TypeVar("T")


class Collection:
    def __init__(self, rules: list[Rule] | None = None):
        self.rules: list[Rule] = [] if rules is None else rules

    def add(self, *rules: Rule) -> None:
        self.rules.extend(rules)
        self.get_parsers_matching_type.cache_clear()

    @overload
    def parse(self, target_type: type[T], source: object) -> T:
        ...

    @overload
    def parse(self, target_type: Any, source: object) -> Any:
        ...

    def parse(self, target_type: object, source: object) -> Any:
        return Controller(self).delegate(target_type, source)

    @lru_cache(1024)
    def get_parsers_matching_type(self, type: object, /) -> list[Callable[[Any, Any, Controller], Any]]:
        return [rule.parser for rule in self.rules if rule.target_condition(type)]
