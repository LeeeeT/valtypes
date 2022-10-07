from __future__ import annotations

from collections import ChainMap
from collections.abc import Mapping
from types import FrameType
from typing import TYPE_CHECKING, Generic, TypeVar
from typing import _GenericAlias as GenericAlias  # type: ignore

from valtypes.util import get_caller_frame

__all__ = ["ForwardRef", "ForwardRefAlias"]


T = TypeVar("T")


if TYPE_CHECKING:

    class ForwardRef(Generic[T]):
        @classmethod
        def evaluate(cls) -> object:
            ...

    class ForwardRefAlias:
        def evaluate(self) -> object:
            ...

else:

    class ForwardRef:
        def __class_getitem__(cls, code: str) -> ForwardRefAlias:
            return ForwardRefAlias(cls, code, get_caller_frame())

    class ForwardRefAlias(GenericAlias, _root=True):
        def __init__(self, origin: type[ForwardRef], code: str, frame: FrameType):
            super().__init__(origin, (code, frame))

        def evaluate(self) -> object:
            return eval(self._code, None, self._namespace)

        @property
        def _namespace(self) -> Mapping[str, object]:
            return ChainMap(self._frame.f_locals, self._frame.f_globals, self._frame.f_builtins)

        @property
        def _code(self) -> str:
            return self.__args__[0]

        @property
        def _frame(self) -> FrameType:
            return self.__args__[1]

        def __repr__(self) -> str:
            return repr(self._code)
