from collections.abc import Callable
from functools import cached_property
from typing import Any, Generic, ParamSpec, cast

from .misc import CompositeCallableDescriptor

__all__ = ["AttributePatcher", "AutoCallSuper", "AutoCallSuperDescriptor", "SuperCallerDescriptor", "super_endpoint"]


P = ParamSpec("P")


def super_endpoint(callable: Callable[P, object]) -> Callable[P, None]:
    return cast(Callable[P, None], AutoCallSuperDescriptor((callable,)))


class AutoCallSuperDescriptor(CompositeCallableDescriptor[P], Generic[P]):  # type: ignore
    pass


class SuperCallerDescriptor:
    def __init__(self, after: type, method_name: str):
        self._after = after
        self._method_name = method_name

    def __get__(self, instance: object, owner: type | None = None) -> Callable[..., None]:
        return getattr(cast(Any, super(cast(Any, self._after), instance)), self._method_name)


class AttributePatcher:
    def __init__(self, owner: type, name: str):
        self._owner = owner
        self._name = name

    def patch_if_needed(self) -> None:
        if self._should_patch:
            self._patch()

    @cached_property
    def _should_patch(self) -> bool:
        return self._attribute_overridden and self._super_attribute_patched

    @cached_property
    def _attribute_overridden(self) -> bool:
        return self._owner_attribute is not self._super_attribute

    @cached_property
    def _owner_attribute(self) -> Any:
        return self._owner.__dict__[self._name]

    @cached_property
    def _super_attribute(self) -> Any:
        for base in self._owner.mro()[1:]:
            if self._name in base.__dict__:
                return base.__dict__[self._name]

    @cached_property
    def _super_attribute_patched(self) -> bool:
        return isinstance(self._super_attribute, AutoCallSuperDescriptor)

    def _patch(self) -> None:
        setattr(self._owner, self._name, self._patched_descriptor)

    @cached_property
    def _patched_descriptor(self) -> AutoCallSuperDescriptor[Any]:
        return AutoCallSuperDescriptor((self._super_caller, self._owner_attribute))

    @cached_property
    def _super_caller(self) -> SuperCallerDescriptor:
        return SuperCallerDescriptor(self._owner, self._name)


class AutoCallSuper:
    def __init_subclass__(cls, *args: object, **kwargs: object) -> None:
        super().__init_subclass__(*args, **kwargs)
        cls._patch_attributes()

    @classmethod
    def _patch_attributes(cls) -> None:
        for attribute_name in cls.__dict__:
            AttributePatcher(cls, attribute_name).patch_if_needed()
