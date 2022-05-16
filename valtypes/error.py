from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from valtypes.util import pretty_type_repr

if TYPE_CHECKING:
    from valtypes import Constrained


__all__ = [
    "BaseParsingError",
    "CompositeParsingError",
    "ConstraintError",
    "ConversionError",
    "FractionalNumberError",
    "MissingFieldError",
    "NoParserError",
    "NotEnoughItemsError",
    "ParsingError",
    "RecursiveParsingError",
    "WrongFieldError",
    "WrongItemError",
    "WrongTypeError",
]


class BaseParsingError(Exception):
    pass


@dataclass
class NoParserError(BaseParsingError):
    source: object
    target_type: object

    def __str__(self) -> str:
        return f"there's no parser for {pretty_type_repr(self.target_type)}"


@dataclass
class RecursiveParsingError(BaseParsingError):
    chain: tuple[object, ...]

    def __str__(self) -> str:
        return "recursion detected: " + " 〉 ".join(map(pretty_type_repr, self.chain))


@dataclass
class ParsingError(BaseParsingError):
    source_type: object
    target_type: object
    cause: BaseParsingError

    def __str__(self) -> str:
        return f"{pretty_type_repr(self.source_type)} 〉 {pretty_type_repr(self.target_type)}: {self.cause}"


@dataclass
class CompositeParsingError(BaseParsingError):
    target_type: object
    causes: tuple[BaseParsingError, ...]

    def __str__(self) -> str:
        result = pretty_type_repr(self.target_type)
        *others, last = map(str, self.causes)
        for other in others:
            result += "\n├ " + other.replace("\n", "\n│ ")
        result += "\n╰ " + last.replace("\n", "\n  ")
        return result


@dataclass
class WrongTypeError(BaseParsingError):
    source: object
    target_type: object

    def __str__(self) -> str:
        return f"not an instance of {pretty_type_repr(self.target_type)}"


@dataclass
class ConversionError(BaseParsingError):
    source: object
    target_type: object

    def __str__(self) -> str:
        return f"can't convert the value to {pretty_type_repr(self.target_type)}"


@dataclass
class ConstraintError(BaseParsingError):
    source: object
    constrained: type[Constrained[Any]]

    def __str__(self) -> str:
        return f"the value doesn't match the {self.constrained.__name__} constraint"


@dataclass
class FractionalNumberError(BaseParsingError):
    number: float

    def __str__(self) -> str:
        return "fractional number"


@dataclass
class WrongItemError(BaseParsingError):
    item: int
    cause: BaseParsingError

    def __str__(self) -> str:
        return f"[{self.item}]: {self.cause}"


@dataclass
class NotEnoughItemsError(BaseParsingError):
    missing_items_count: int

    def __str__(self) -> str:
        if self.missing_items_count == 1:
            return "1 item is missing"
        return f"{self.missing_items_count} items are missing"


@dataclass
class WrongFieldError(BaseParsingError):
    field: str
    cause: BaseParsingError

    def __str__(self) -> str:
        return f"[{self.field}]: {self.cause}"


@dataclass
class MissingFieldError(BaseParsingError):
    field: str

    def __str__(self) -> str:
        return f"[{self.field}]: required field is missing"
