from __future__ import annotations

from typing import TypeVar

from valtypes.parsing.controller import Controller
from valtypes.util import resolve_type_args

__all__ = ["list_to_variable_length_tuple"]


T = TypeVar("T")


def list_to_variable_length_tuple(target_type: type[tuple[T, ...]], source: object, controller: Controller) -> tuple[T, ...]:
    return tuple(controller.delegate(list[resolve_type_args(target_type, tuple)], source))  # type: ignore
