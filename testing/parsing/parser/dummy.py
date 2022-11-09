from __future__ import annotations

from dataclasses import dataclass
from typing import NoReturn

from valtypes.parsing.parser import ABC

__all__ = ["Dummy"]


@dataclass(init=False, repr=False)
class Dummy(ABC[object, NoReturn]):
    _type: object

    def __init__(self, type: object):
        self._type = type

    def parse(self, source: object, /) -> NoReturn:
        raise NotImplementedError
