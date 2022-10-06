from typing import TYPE_CHECKING, Annotated, TypeVar

from .collection import Collection
from .parsing import parse

__version__ = "3.0.2"

__all__ = [
    "Collection",
    "Ref",
    "parse",
]


T = TypeVar("T")


if TYPE_CHECKING:
    Ref = Annotated[T, ...]
else:
    from .forward_ref import ForwardRef as Ref
