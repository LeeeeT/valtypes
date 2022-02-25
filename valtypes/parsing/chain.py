from __future__ import annotations

from collections.abc import Iterable, Sequence
from types import UnionType
from typing import TYPE_CHECKING, Any, NamedTuple

from . import parser
from .rule import Rule

if TYPE_CHECKING:
    from .collection import Collection


__all__ = ["Node", "Chain", "create_chains"]


class Node(NamedTuple):
    target_type: object
    parser: parser.ABC

    def parse(self, source: object, collection: Collection) -> Any:
        return self.parser.parse(self.target_type, source, collection)


class Chain:
    def __init__(self, *nodes: Node):
        self._nodes = nodes

    @property
    def nodes(self) -> tuple[Node, ...]:
        return self._nodes

    def parse(self, source: object, collection: Collection) -> Any:
        for node in self._nodes:
            source = node.parse(source, collection)
        return source


class ChainsCreator:
    def __init__(self, source_type: type, rules: Iterable[Rule]):
        self._source_type = source_type
        self._rules = list(rules)
        self._explored: set[Node] = set()

    def create_chains(self, target_type: object) -> Iterable[Chain]:
        if isinstance(target_type, UnionType):
            yield from self._process_union(target_type)
        else:
            yield from self._process_type(target_type)

    def _process_union(self, target_union: UnionType) -> Iterable[Chain]:
        for choice in target_union.__args__:
            yield from self.create_chains(choice)

    def _process_type(self, target_type: object) -> Iterable[Chain]:
        if isinstance(target_type, type) and issubclass(self._source_type, target_type):
            yield Chain()
        else:
            yield from self._chains_according_rules(target_type)

    def _chains_according_rules(self, target_type: object) -> Iterable[Chain]:
        for rule in self._rules:
            new_node = Node(target_type, rule.parser)
            if new_node not in self._explored and rule.check(target_type):
                self._explored.add(new_node)
                yield from (Chain(*chain.nodes, new_node) for chain in self.create_chains(rule.source_type))


def create_chains(source_type: type, target_type: object, rules: Iterable[Rule]) -> Iterable[Chain]:
    return ChainsCreator(source_type, rules).create_chains(target_type)
