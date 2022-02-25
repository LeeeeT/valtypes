from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import Any, TypeVar, overload

from valtypes import condition

from . import parser
from .chain import create_chains
from .error import NoParserFoundError, ParsingError
from .rule import Rule

T = TypeVar("T")

T_Parser = TypeVar("T_Parser", bound=parser.ABC)


__all__ = ["Collection"]


class Collection:
    def __init__(self, *rules: Rule):
        self._rules = list(rules)

    @property
    def rules(self) -> Sequence[Rule]:
        return self._rules

    def add(self, *rules: Rule) -> None:
        self._rules.extend(rules)

    def register(
        self, *, source_type: object = object, target_condition: condition.ABC[object] | None = None
    ) -> Callable[[T_Parser], T_Parser]:
        def registrar(parser: T_Parser) -> T_Parser:
            self.add(Rule(parser, source_type=source_type, target_condition=target_condition))
            return parser

        return registrar

    @overload
    def parse(self, target_type: type[T], source: object) -> T:
        ...

    @overload
    def parse(self, target_type: Any, source: object) -> Any:
        ...

    def parse(self, target_type: object, source: object) -> Any:
        for chain in create_chains(type(source), target_type, self._rules):
            try:
                return chain.parse(source, self)
            except ParsingError:
                pass
        raise NoParserFoundError(target_type, source)
