from typing import NoReturn

import valtypes.error.parsing as error
from valtypes.parsing.parser import ABC

__all__ = ["AlwaysRaise"]


class AlwaysRaise(ABC[object, NoReturn]):
    def __init__(self, error: error.Base):
        self._error = error

    def parse(self, source: object, /) -> NoReturn:
        raise self._error
