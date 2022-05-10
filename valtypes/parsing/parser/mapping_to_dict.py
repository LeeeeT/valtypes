from __future__ import annotations

from collections.abc import Mapping
from typing import TypeVar

from valtypes.parsing.controller import Controller
from valtypes.parsing.util import with_source_type
from valtypes.util import resolve_type_args

__all__ = ["mapping_to_dict"]


T = TypeVar("T")
F = TypeVar("F")


@with_source_type(Mapping)
def mapping_to_dict(target_type: type[dict[T, F]], source: Mapping[object, object], controller: Controller) -> dict[T, F]:
    keys_type, values_type = resolve_type_args(target_type, dict)
    return {controller.parse(keys_type, key): controller.parse(values_type, value) for key, value in source.items()}
