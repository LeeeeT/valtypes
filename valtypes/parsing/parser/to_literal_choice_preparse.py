from typing import TypeVar

import valtypes.error.parsing as error
import valtypes.error.parsing.literal as literal_error

from .base import ABC
from .to_literal_choice import ToLiteralChoice

__all__ = ["ToLiteralChoicePreparse"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ToLiteralChoicePreparse(ABC[T_contra, T_co]):
    def __init__(self, choice_parser: ToLiteralChoice[T_co], preparser: ABC[T_contra, T_co]):
        self._choice_parser = choice_parser
        self._preparser = preparser

    def parse(self, source: T_contra, /) -> T_co:
        try:
            intermediate_result = self._preparser.parse(source)
        except error.Base as e:
            raise literal_error.InvalidValue(self._choice_parser.choice, e, source) from None
        return self._choice_parser.parse(intermediate_result)
