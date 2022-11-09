These types are subclasses of built-in `frozenset` type with some constraints on it.

## `InitHook`

Type with special `__init_hook__` method which is called on instantiation. It can be used to perform some additional checks on the value.

```python
from valtypes.type.frozenset import InitHook
from valtypes.error.parsing import Base as ParsingError


class EvenNumbers(InitHook[int]):
    def __init_hook__(self) -> None:
        if any(n % 2 for n in self):
            raise ParsingError(f"{self.__class__.__name__} can't contain odd numbers")


EvenNumbers({2, 4, 6})  # passes
EvenNumbers({2, 3, 6})  # raises ParsingError
```

## `MinimumLength`

Type for representing a `frozenset` that has a given minimum length. The minimum allowed length is stored in the `__minimum_length__` attribute.

```python
from typing import TypeVar

from valtypes.type.frozenset import MinimumLength


T_co = TypeVar("T_co", covariant=True)


class AtLeastTwoElements(MinimumLength[T_co]):
    __minimum_length__ = 2


AtLeastTwoElements({1, 2})  # passes
AtLeastTwoElements({1})  # raises valtypes.error.parsing.type.sized.MinimumLength
```

## `MaximumLength`

Type for representing a `frozenset` that has a given maximum length. The maximum allowed length is stored in the `__maximum_length__` attribute.

```python
from typing import TypeVar

from valtypes.type.frozenset import MaximumLength


T_co = TypeVar("T_co", covariant=True)


class AtMostTwoElements(MaximumLength[T_co]):
    __maximum_length__ = 2


AtMostTwoElements({1, 2})  # passes
AtMostTwoElements({1, 2, 3})  # raises valtypes.error.parsing.type.sized.MaximumLength
```

## `NonEmpty`

Type for representing a non-empty `frozenset`. It is a subclass of `MinimumLength` with `__minimum_length__` set to `1`.

```python
from valtypes.type.frozenset import NonEmpty

NonEmpty({1})  # passes
NonEmpty()  # raises valtypes.error.parsing.type.sized.MinimumLength
```
