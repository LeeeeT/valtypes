from __future__ import annotations

import inspect

from regex import Match, Pattern

from valtypes.typing import HasModuleAndName

from .resolve_type_args import resolve_type_args
from .static_analysis import static_analysis

__all__ = ["resolve_type_args", "static_analysis", "get_caller_namespace", "get_absolute_name", "strict_match"]


def get_caller_namespace() -> dict[str, object]:
    frame = inspect.stack()[2][0]
    return frame.f_builtins | frame.f_globals | frame.f_locals


def get_absolute_name(obj: HasModuleAndName, /) -> str:
    return f"{obj.__module__}.{obj.__name__}"


def strict_match(pattern: Pattern[str], string: str) -> Match[str]:
    match = pattern.fullmatch(string)
    if match is None:
        raise ValueError
    return match
