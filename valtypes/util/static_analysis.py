from __future__ import annotations

from typing import TYPE_CHECKING

__all__ = ["static_analysis"]


if TYPE_CHECKING:
    from dataclasses import dataclass as static_analysis
else:

    def static_analysis(cls=None, *, kw_only=None):
        return (lambda cls: cls) if cls is None else cls
