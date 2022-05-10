from __future__ import annotations

from typing import Any
from typing import _LiteralGenericAlias as LiteralGenericAlias  # type: ignore

from valtypes.error import ConversionError
from valtypes.parsing.controller import Controller

__all__ = ["to_literal"]


def to_literal(target_type: LiteralGenericAlias, source: object, controller: Controller) -> Any:
    for choice in target_type.__args__:
        parsed = controller.delegate(type(choice), source)
        if parsed == choice:
            return parsed
    raise ConversionError(source, target_type)
