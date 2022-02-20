from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["ABC"]


T = TypeVar("T")


class ABC(abc.ABC):
    @abc.abstractmethod
    def parse(self, target_type: Any, value: Any, collection: Collection) -> Any:
        pass
