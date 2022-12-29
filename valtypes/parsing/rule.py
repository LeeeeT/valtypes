from typing import Any, Generic, TypeVar

from valtypes import condition
from valtypes.parsing import parser
from valtypes.parsing.factory import ABC as ABCFactory

__all__ = ["Rule"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class Rule(Generic[T_contra, T_co]):
    def __init__(self, factory: ABCFactory[Any, T_contra, T_co], type_condition: condition.ABC[object]):
        self._factory = factory
        self._type_condition = type_condition

    def is_suitable_for(self, type: object) -> bool:
        return self._type_condition.check(type)

    def get_parser_for(self, type: Any) -> parser.ABC[T_contra, T_co]:
        return self._factory.get_parser_for(type)
