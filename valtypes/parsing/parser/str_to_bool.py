from __future__ import annotations

from valtypes.error import ConversionError
from valtypes.parsing.controller import Controller
from valtypes.parsing.util import with_source_type

__all__ = ["str_to_bool"]


TRUE = {"1", "on", "t", "true", "y", "yes"}
FALSE = {"0", "off", "f", "false", "n", "no"}


@with_source_type(str)
def str_to_bool(target_type: type[bool], source: str, controller: Controller) -> bool:
    if source.lower() in TRUE:
        return True
    if source.lower() in FALSE:
        return False
    raise ConversionError(source, target_type)
