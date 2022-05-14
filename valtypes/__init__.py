import importlib.metadata
from typing import TYPE_CHECKING, Annotated, TypeVar

from .alias import Alias
from .collection import Collection
from .constrained import Constrained
from .error import BaseParsingError, ConstraintError
from .parsing import parse

__version__ = importlib.metadata.version("valtypes")

__all__ = [
    "Alias",
    "BaseParsingError",
    "Collection",
    "Constrained",
    "ConstraintError",
    "ForwardRef",
    "parse",
]


T = TypeVar("T")


if TYPE_CHECKING:
    ForwardRef = Annotated[T, ...]
else:
    from .forward_ref import ForwardRef
