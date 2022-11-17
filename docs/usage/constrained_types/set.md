These types are subclasses of built-in `set` type with some constraints on it.

## `InitHook`

Type with special `__init_hook__` method which is called on instantiation. It is not intended to be used without other hooks, because it does **not** guarantee that the `set` won't be modified later in the program.

```python
from valtypes.type.set import InitHook
from valtypes.error.parsing import Base as ParsingError


class EvenNumbers(InitHook[int]):
    def __init_hook__(self) -> None:
        if any(n % 2 for n in self):
            raise ParsingError(f"{self.__class__.__name__} can't contain odd numbers")


EvenNumbers({2, 4, 6})  # passes
EvenNumbers({2, 3, 6})  # raises ParsingError
```

!!! warning
    The code above does **not** keep the `set` from being modified after instantiation. It can still contain odd numbers. If you want to prevent that, you can use immutable types like `frozenset` instead.

## `LengthHook`

Type with special `__length_hook__` method which is called whenever the length of a `set` is going to change. Calling methods like `add` or `update` as well as assignment operators will trigger this hook with the new length that the `set` would have after the operation.

If the hook raises an exception, the operation is aborted and the `set` is left unchanged.

```python
from valtypes.type.set import LengthHook
from valtypes.error.parsing import Base as ParsingError


class WithEvenLength(LengthHook[int]):
    def __length_hook__(self, new_length: int) -> None:
        if new_length % 2:
            raise ParsingError(f"{self.__class__.__name__} can't have odd length")


l = WithEvenLength({1, 2})
l.update({3, 4})  # passes
l.discard(5)  # nothing to discard, so it passes

try:
    l.pop()  # raises ParsingError
    # because the set would have odd length after this operation
except ParsingError:
    # thus, the set is not modified
    print(l)  # {1, 2, 3, 4}
```

## `MinimumLength`

Type for representing a `set` that has a given minimum length. The minimum allowed length is stored in the `__minimum_length__` attribute.

```python
from typing import TypeVar

from valtypes.type.set import MinimumLength


T = TypeVar("T")


class AtLeastTwoElements(MinimumLength[T]):
    __minimum_length__ = 2


s = AtLeastTwoElements({1, 2})  # passes
s &= {2, 3}  # raises valtypes.error.parsing.type.sized.MinimumLength
```

## `MaximumLength`

Type for representing a `set` that has a given maximum length. The maximum allowed length is stored in the `__maximum_length__` attribute.

```python
from typing import TypeVar

from valtypes.type.set import MaximumLength


T = TypeVar("T")


class AtMostTwoElements(MaximumLength[T]):
    __maximum_length__ = 2


s = AtMostTwoElements({1, 2})  # passes
s |= {2, 3}  # raises valtypes.error.parsing.type.sized.MaximumLength
```

## `NonEmpty`

Type for representing a non-empty `set`. It is a subclass of `MinimumLength` with `__minimum_length__` set to `1`.

```python
from valtypes.type.set import NonEmpty

s = NonEmpty({1})  # passes
s.clear()  # raises valtypes.error.parsing.type.sized.MinimumLength
```
