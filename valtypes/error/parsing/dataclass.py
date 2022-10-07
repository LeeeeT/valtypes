from dataclasses import dataclass

from .generic import Base

__all__ = ["MissingField", "WrongFieldValue"]


@dataclass
class WrongFieldValue(Base):
    field: str
    cause: Base

    def __str__(self) -> str:
        return f"[{self.field}]: {self.cause}"


@dataclass
class MissingField(Base):
    field: str

    def __str__(self) -> str:
        return f"[{self.field}]: required field is missing"
