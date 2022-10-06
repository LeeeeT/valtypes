from dataclasses import dataclass

from valtypes.error import base

__all__ = ["MissingField", "WrongFieldValue"]


@dataclass
class WrongFieldValue(base.Base):
    field: str
    cause: base.Base

    def __str__(self) -> str:
        return f"[{self.field}]: {self.cause}"


@dataclass
class MissingField(base.Base):
    field: str

    def __str__(self) -> str:
        return f"[{self.field}]: required field is missing"
