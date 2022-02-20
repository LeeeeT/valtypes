from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import Any, TypeVar
from typing import _SpecialForm as SpecialForm  # noqa
from typing import overload

from valtypes.typing import GenericAlias

from . import parser
from .path_finder import PathFinder
from .rule import Rule

T = TypeVar("T")

T_Parser = TypeVar("T_Parser", bound=parser.ABC)


__all__ = ["Collection"]


class Collection:
    def __init__(self, *rules: Rule):
        self._rules = list(rules)
        self._path_finder = PathFinder(self._rules)

    @property
    def rules(self) -> Sequence[Rule]:
        return self._rules

    def add(self, *rules: Rule) -> None:
        self._rules.extend(rules)

    def register(self, *, source_type: object = object, target_type: object = object) -> Callable[[T_Parser], T_Parser]:
        def registrar(parser: T_Parser) -> T_Parser:
            self.add(Rule(parser, source_type=source_type, target_type=target_type))
            return parser

        return registrar

    @overload
    def parse(self, target_type: type[T], source: object) -> T:
        ...

    @overload
    def parse(self, target_type: Any, source: object) -> Any:
        ...

    def parse(self, target_type: object, source: object) -> Any:
        if (
            isinstance(target_type, type)
            and not isinstance(target_type, GenericAlias)
            and issubclass(type(source), target_type)
        ):
            return source

        path = self._path_finder.find_path(type(source), target_type)
        target_types = [rule.source_type for rule in path[1:]] + [target_type]

        for rule, target_type in zip(path, target_types):
            source = rule.parser.parse(target_type, source, self)
        return source
