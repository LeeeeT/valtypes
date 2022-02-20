from __future__ import annotations

from typing import TYPE_CHECKING

from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["str_to_bool"]


TRUE = {"1", "on", "t", "true", "y", "yes"}
FALSE = {"0", "off", "f", "false", "n", "no"}


@convert
def str_to_bool(target_type: type[bool], source: str, collection: Collection) -> bool:
    if source.lower() in TRUE:
        return True
    if source.lower() in FALSE:
        return False
    raise ParsingError(bool, source)
