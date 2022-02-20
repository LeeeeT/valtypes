from __future__ import annotations

from functools import reduce
from operator import or_

from .util import get_absolute_name

__all__ = ["Dataclass"]


class Dataclass:
    def __init__(self, *args: object, **kwargs: object):
        for field, value in zip(tuple(kwargs.keys()) + tuple(self.__all_annotations__), tuple(kwargs.values()) + args):
            setattr(self, field, value)

    @classmethod
    @property
    def __all_annotations__(cls) -> dict[str, object]:
        return reduce(
            or_,
            (base.__dict__.get("__annotations__", {}) for base in reversed(cls.mro()) if issubclass(base, Dataclass)),
            {},
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dataclass):
            return NotImplemented
        return self.__all_annotations__.keys() <= other.__all_annotations__.keys() and all(
            getattr(self, field) == getattr(other, field) for field in self.__all_annotations__
        )

    def as_dict(self) -> dict[str, object]:
        intermediate_result: dict[str, object] = {}
        for field in self.__all_annotations__:
            value = getattr(self, field)
            intermediate_result[field] = value.as_dict() if isinstance(value, Dataclass) else value
        return intermediate_result

    def __repr__(self) -> str:
        fields = (f"{field}={getattr(self, field)!r}" for field in self.__all_annotations__)
        return f"{get_absolute_name(self.__class__)}({', '.join(fields)})"  # type: ignore
