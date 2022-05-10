from typing import Any

from valtypes.error import BaseParsingError, CompositeParsingError
from valtypes.parsing.controller import Controller
from valtypes.typing import UnionType

__all__ = ["to_union"]


def to_union(target_type: UnionType, source: object, controller: Controller) -> Any:
    errors: list[BaseParsingError] = []
    for choice in target_type.__args__:
        try:
            return controller.delegate(choice, source)
        except BaseParsingError as error:
            errors.append(error)
    raise CompositeParsingError(target_type, tuple(errors))
