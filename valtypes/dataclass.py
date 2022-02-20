from typing import TYPE_CHECKING

from .util import get_absolute_name

__all__ = ["Dataclass"]


class DataclassMeta(type):
    def __init__(cls, name: str, bases: tuple[type, ...], attrs: dict[str, object]):
        super().__init__(name, bases, attrs)
        cls.__all_annotations__: dict[str, object] = {}
        cls._collect_annotations()

    def _collect_annotations(cls) -> None:
        all_annotations = [getattr(base, "__annotations__", {}) for base in cls.mro()]
        for annotations in reversed(all_annotations):
            cls.__all_annotations__.update(annotations)


class Dataclass(metaclass=DataclassMeta):
    if TYPE_CHECKING:
        __all_annotations__: dict[str, object]

    def __init__(self, *args: object, **kwargs: object):
        for field, value in zip(tuple(kwargs.keys()) + tuple(self.__all_annotations__), tuple(kwargs.values()) + args):
            setattr(self, field, value)

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
        return f"{get_absolute_name(self.__class__)}({', '.join(fields)})"
