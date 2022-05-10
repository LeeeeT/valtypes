from __future__ import annotations

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
    "WrongFieldError",
    "WrongItemError",
    "WrongTypeError",
]


class BaseParsingError(Exception):
    pass


class NoParserError(BaseParsingError):
    def __init__(self, source: object, target_type: object):
        self.source = source
        self.target_type = target_type

    def __str__(self) -> str:
        return f"there's no parser for {pretty_type_repr(self.target_type)}"


class ParsingError(BaseParsingError):
    def __init__(self, source_type: object, target_type: object, cause: BaseParsingError):
        self.source_type = source_type
        self.target_type = target_type
        self.cause = cause

    def __str__(self) -> str:
        return f"{pretty_type_repr(self.source_type)} 〉 {pretty_type_repr(self.target_type)}: {self.cause}"


class CompositeParsingError(ParsingError):
    def __init__(self, target_type: object, causes: tuple[BaseParsingError, ...]):
        self.target_type = target_type
        self.causes = causes

    def __str__(self) -> str:
        result = pretty_type_repr(self.target_type)
        *others, last = map(str, self.causes)
        for other in others:
            result += "\n├ " + other.replace("\n", "\n│ ")
        result += "\n╰ " + last.replace("\n", "\n  ")
        return result


class WrongTypeError(BaseParsingError):
    def __init__(self, source: object, target_type: object):
        self.source = source
        self.target_type = target_type

    def __str__(self) -> str:
        return f"not an instance of {pretty_type_repr(self.target_type)}"


class ConversionError(BaseParsingError):
    def __init__(self, source: object, target_type: object):
        self.source = source
        self.target_type = target_type

    def __str__(self) -> str:
        return f"can't convert the value to {pretty_type_repr(self.target_type)}"


class ConstraintError(BaseParsingError):
    def __init__(self, source: object, constrained: type[Constrained[Any]]):
        self.source = source
        self.constrained = constrained

    def __str__(self) -> str:
        return f"the value does not match the {self.constrained.__name__} constraint"


class FractionalNumberError(BaseParsingError):
    def __init__(self, number: float):
        self.number = number

    def __str__(self) -> str:
        return "fractional number"


class WrongItemError(BaseParsingError):
    def __init__(self, item: int, cause: BaseParsingError):
        self.item = item
        self.cause = cause

    def __str__(self) -> str:
        return f"[{self.item}]: {self.cause}"


class NotEnoughItemsError(BaseParsingError):
    def __init__(self, missing_items_count: int):
        self.missing_items_count = missing_items_count

    def __str__(self) -> str:
        if self.missing_items_count == 1:
            return "1 item is missing"
        return f"{self.missing_items_count} items are missing"


class WrongFieldError(BaseParsingError):
    def __init__(self, field: str, cause: BaseParsingError):
        self.field = field
        self.cause = cause

    def __str__(self) -> str:
        return f"[{self.field}]: {self.cause}"


class MissingFieldError(BaseParsingError):
    def __init__(self, field: str):
        self.field = field

    def __str__(self) -> str:
        return f"[{self.field}]: required field is missing"
