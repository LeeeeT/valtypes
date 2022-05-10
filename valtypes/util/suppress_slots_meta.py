from typing import TypeVar

__all__ = ["SuppressSlotsMeta"]


T_SuppressSlotsMeta = TypeVar("T_SuppressSlotsMeta", bound="SuppressSlotsMeta")


class SuppressSlotsMeta(type):
    def __new__(mcs: type[T_SuppressSlotsMeta], name: str, bases: tuple[type, ...], attrs: dict[str, object], **kwargs: object) -> T_SuppressSlotsMeta:
        attrs["__slots__"] = ()
        return super().__new__(mcs, name, bases, attrs, **kwargs)
