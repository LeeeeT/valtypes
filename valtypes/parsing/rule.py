from valtypes import condition

from . import parser

__all__ = ["Rule"]


class Rule:
    def __init__(
        self, parser: parser.ABC, *, source_type: object = object, target_condition: condition.ABC[object] | None = None
    ):
        self.parser = parser
        self.source_type = source_type
        self.target_condition = condition.truthy if target_condition is None else target_condition

    def check(self, target_type: object) -> bool:
        return self.target_condition.check(target_type)
