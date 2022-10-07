from __future__ import annotations

from typing import NoReturn

from valtypes.parsing.parser import ABC

__all__ = ["Dummy"]


class Dummy(ABC[object, NoReturn]):
    def __init__(self, type: object):
        self._type = type

    def parse(self, source: object, /) -> NoReturn:
        raise NotImplementedError

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, Dummy):
            return self._type == other._type
        return NotImplemented
