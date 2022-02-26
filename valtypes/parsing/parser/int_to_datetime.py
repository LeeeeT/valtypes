from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["int_to_datetime"]


@convert
def int_to_datetime(target_type: datetime, source: int, collection: Collection) -> datetime:
    return datetime.utcfromtimestamp(source)
