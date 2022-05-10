from __future__ import annotations

import inspect
from collections import ChainMap
from types import FrameType
from typing import TypeVar

__all__ = ["ForwardRef"]

T_ForwardRef = TypeVar("T_ForwardRef", bound="ForwardRef")


class ForwardRef:
    def __init__(self, code: str, frame: FrameType):
        self.code = code
        self.frame = frame

    def __class_getitem__(cls: type[T_ForwardRef], code: str, /) -> T_ForwardRef:
        return cls(code, inspect.stack()[1][0])

    def evaluate(self) -> object:
        return eval(self.code, None, ChainMap(self.frame.f_locals, self.frame.f_globals, self.frame.f_builtins))
