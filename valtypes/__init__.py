from typing import TYPE_CHECKING, Annotated, TypeVar

from .collection import Collection
from .parsing import parse_json

__version__ = "7.0.0"

__all__ = [
    "Collection",
    "Ref",
    "parse_json",
]


T = TypeVar("T")


if TYPE_CHECKING:
    Ref = Annotated[T, ...]
else:
    from .forward_ref import ForwardRef as Ref
