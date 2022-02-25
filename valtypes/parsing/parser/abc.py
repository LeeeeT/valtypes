from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["ABC"]


class ABC(abc.ABC):
    @abc.abstractmethod
    def parse(self, target_type: Any, source: Any, collection: Collection) -> Any:
        pass
