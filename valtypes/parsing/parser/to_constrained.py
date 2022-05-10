from __future__ import annotations

from typing import Any, TypeVar

from valtypes.constrained import Constrained
from valtypes.parsing.controller import Controller
from valtypes.util import resolve_type_args

__all__ = ["to_constrained"]


T_Constrained = TypeVar("T_Constrained", bound=Constrained[Any])


def to_constrained(target_type: type[T_Constrained], source: object, controller: Controller) -> T_Constrained:
    return target_type(controller.delegate(resolve_type_args(target_type, Constrained)[0], source))
