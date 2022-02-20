from typing import Any

from valtypes import condition

__all__ = ["ConstraintError"]


class ConstraintError(ValueError):
    def __init__(self, value: object, constraint: condition.ABC[Any]):
        super().__init__(f"value {value!r} does not satisfy constraint {constraint!r}")
        self.value = value
        self.constraint = constraint
