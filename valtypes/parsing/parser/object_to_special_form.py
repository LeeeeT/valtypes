from __future__ import annotations

from typing import TYPE_CHECKING, Any
from typing import _SpecialForm as SpecialForm  # noqa

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["object_to_special_form"]


@convert
def object_to_special_form(target_type: SpecialForm, source: object, collection: Collection) -> Any:
    return source
