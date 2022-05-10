from __future__ import annotations

from typing import TypeVar

from valtypes.parsing.controller import Controller
from valtypes.util import resolve_type_args

__all__ = ["list_to_set"]


T = TypeVar("T")


def list_to_set(target_type: type[set[T]], source: object, controller: Controller) -> set[T]:
    return set(controller.delegate(list[resolve_type_args(target_type, set)], source))  # type: ignore
