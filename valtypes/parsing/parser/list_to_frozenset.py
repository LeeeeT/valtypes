from __future__ import annotations

from typing import TypeVar

from valtypes.parsing.controller import Controller
from valtypes.util import resolve_type_args

__all__ = ["list_to_frozenset"]


T = TypeVar("T")


def list_to_frozenset(target_type: type[frozenset[T]], source: object, controller: Controller) -> frozenset[T]:
    return frozenset(controller.delegate(list[resolve_type_args(target_type, frozenset)], source))  # type: ignore
