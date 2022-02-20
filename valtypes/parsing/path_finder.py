from collections.abc import Sequence
from types import UnionType
from typing import _SpecialForm as SpecialForm  # noqa

from valtypes.typing import GenericAlias

from .error import NoParserFoundError
from .rule import Rule

__all__ = ["PathFinder"]


class PathFinder:
    _source_type: type
    _target_type: object

    _explored: list[Rule]
    _queue: list[list[Rule]]

    _current_path: list[Rule]
    _current_parent_rule: Rule

    _found_path: list[Rule] | None

    def __init__(self, rules: Sequence[Rule]):
        self._rules = rules

    def find_path(self, source_type: type, target_type: object) -> list[Rule]:
        self._source_type = source_type
        self._target_type = target_type
        self._initialize()
        self._process_queue()
        if self._found_path is None:
            raise NoParserFoundError(self._source_type, self._target_type)
        return self._found_path

    def _initialize(self) -> None:
        self._found_path = None
        self._explored = []
        self._queue = [
            [rule]
            for rule in self._rules
            if isinstance(rule.source_type, type) and issubclass(self._source_type, rule.source_type)
        ]

    def _process_queue(self) -> None:
        while self._queue:
            self._current_path = self._queue.pop(0)
            self._process_path()

    def _process_path(self) -> None:
        self._current_parent_rule = self._current_path[-1]
        if types_match(self._target_type, self._current_parent_rule.target_type):
            self._found_path = self._current_path
            self._queue.clear()
        elif self._current_parent_rule not in self._explored:
            self._process_parent_rule()

    def _process_parent_rule(self) -> None:
        self._explored.append(self._current_parent_rule)
        for child_rule in filter(
            lambda rule: types_match(rule.source_type, self._current_parent_rule.target_type), self._rules
        ):
            self._queue.append(self._current_path + [child_rule])


def types_match(type_1: object, type_2: object) -> bool:
    if isinstance(type_2, (type, UnionType)):
        return issubclass(determine_type(type_1), type_2)
    return type_1 is type_2


def determine_type(typ: object) -> type:
    if isinstance(typ, GenericAlias):
        return typ.__origin__  # type: ignore
    if isinstance(typ, type):
        return typ
    return type(typ)
