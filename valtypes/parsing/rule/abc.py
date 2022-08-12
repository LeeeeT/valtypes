import abc
from typing import Any, Generic, TypeVar

from valtypes.parsing import parser

__all__ = ["ABC"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ABC(abc.ABC, Generic[T_contra, T_co]):
    @abc.abstractmethod
    def is_suitable_for(self, type: object) -> bool:
        pass

    @abc.abstractmethod
    def get_parser_for(self, type: Any) -> parser.ABC[T_contra, T_co]:
        pass
