from typing import TypeVar

from valtypes.error import WrongTypeError
from valtypes.parsing.controller import Controller
from valtypes.typing import GenericAlias

__all__ = ["object_to_type"]


T = TypeVar("T")


def object_to_type(target_type: type[T], source: object, controller: Controller) -> T:
    if not isinstance(target_type, GenericAlias) and isinstance(source, target_type):
        return source
    raise WrongTypeError(source, target_type)
