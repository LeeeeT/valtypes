These types are subclasses of built-in `list` type with some constraints on it.

## `InitHook`

Type with special `__init_hook__` method which is called on instantiation. It is not intended to be used without other hooks, because it does **not** guarantee that the `list` won't be modified later in the program.

```python
from valtypes.type.list import InitHook
from valtypes.error.parsing import Base as ParsingError


class EvenNumbers(InitHook[int]):
    def __init_hook__(self) -> None:
        if any(n % 2 for n in self):
            raise ParsingError(f"{self.__class__.__name__} can't contain odd numbers")


EvenNumbers([2, 4, 6])  # passes
EvenNumbers([2, 3, 6])  # raises ParsingError
```

!!! warning
    The code above does **not** keep the `list` from being modified after instantiation. It can still contain odd numbers. If you want to prevent that, you can use immutable types like `tuple` instead.

## `LengthHook`

Type with special `__length_hook__` method which is called whenever the length of a `list` is going to change. Calling methods like `append` or `extend` as well as assignment operators will trigger this hook with the new length that the `list` would have after the operation.

If the hook raises an exception, the operation is aborted and the `list` is left unchanged.

```python
from valtypes.type.list import LengthHook
from valtypes.error.parsing import Base as ParsingError


class WithEvenLength(LengthHook[int]):
    def __length_hook__(self, new_length: int) -> None:
        if new_length % 2:
            raise ParsingError(f"{self.__class__.__name__} can't have odd length")


l = WithEvenLength([1, 2, 3, 4])
l.extend([5, 6])  # passes
del l[:2]  # passes

try:
    l.pop()  # raises ParsingError
    # because the list would have odd length after this operation
except ParsingError:
    # thus, the list is not modified
    print(l)  # [3, 4, 5, 6]
```

## `MinimumLength`

Type for representing a `list` that has a given minimum length. The minimum allowed length is stored in the `__minimum_length__` attribute.

```python
from typing import TypeVar

from valtypes.type.list import MinimumLength


T = TypeVar("T")


class AtLeastTwoElements(MinimumLength[T]):
    __minimum_length__ = 2


l = AtLeastTwoElements([1, 2])  # passes
l[:] = [3, 4]  # passes
l.clear()  # raises valtypes.error.parsing.type.sized.MinimumLength
```

## `MaximumLength`

Type for representing a `list` that has a given maximum length. The maximum allowed length is stored in the `__maximum_length__` attribute.

```python
from typing import TypeVar

from valtypes.type.list import MaximumLength


T = TypeVar("T")


class AtMostTwoElements(MaximumLength[T]):
    __maximum_length__ = 2


l = AtMostTwoElements()  # passes
l.extend([1, 2])  # passes
l.append(3)  # raises valtypes.error.parsing.type.sized.MaximumLength
```

## `NonEmpty`

Type for representing a non-empty `list`. It is a subclass of `MinimumLength` with `__minimum_length__` set to `1`.

```python
from valtypes.type.list import NonEmpty

l = NonEmpty([1])  # passes
l.pop()  # raises valtypes.error.parsing.type.sized.MinimumLength
```
