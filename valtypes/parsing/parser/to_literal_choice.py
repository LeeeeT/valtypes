from typing import Final, TypeVar

import valtypes.error.parsing.literal as error

from .abc import ABC

__all__ = ["ToLiteralChoice"]


T = TypeVar("T")


class ToLiteralChoice(ABC[T, T]):
    def __init__(self, choice: T):
        self.choice: Final = choice

    def parse(self, source: T, /) -> T:
        if source == self.choice:
            return source
        raise error.NotMember(self.choice, source)
