from typing import Any, TypeVar

from valtypes.parsing import parser
from valtypes.typing import LiteralAlias

from .base import ABC

__all__ = ["ToLiteral"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ToLiteral(ABC[LiteralAlias, T_contra, T_co]):
    def __init__(self, factory: ABC[Any, T_contra, T_co]):
        self._factory = factory

    def get_parser_for(self, type_: LiteralAlias, /) -> parser.ToLiteral[T_contra, T_co]:
        return parser.ToLiteral(
            [
                parser.ToLiteralChoicePreparse[T_contra, T_co](parser.ToLiteralChoice(choice), self._factory.get_parser_for(type(choice)))
                for choice in type_.__args__
            ]
        )
