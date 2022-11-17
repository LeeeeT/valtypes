These types are subclasses of built-in `int` type with some constraints on it.

## `InitHook`

Type with special `__init_hook__` method which is called on instantiation. It can be used to perform some additional checks on the value.

```python
from valtypes.type.int import InitHook
from valtypes.error.parsing import Base as ParsingError


class MultipleOf3(InitHook):
    def __init_hook__(self) -> None:
        if self % 3:
            raise ParsingError(f"{self} is not a multiple of 3")


MultipleOf3(3)  # passes
MultipleOf3(4)  # raises ParsingError
```

## `Maximum`

Type for representing an `int` that is less than or equal to a given maximum. The maximum allowed value is stored in the `__maximum__` attribute.

```python
from valtypes.type.int import Maximum


class LessEqualsTen(Maximum):
    __maximum__ = 10


LessEqualsTen(9)  # passes
LessEqualsTen(10)  # passes
LessEqualsTen(11)  # raises valtypes.error.parsing.type.numeric.Maximum
```

## `Minimum`

Type for representing an `int` that is greater than or equal to a given minimum. The minimum allowed value is stored in the `__minimum__` attribute.

```python
from valtypes.type.int import Minimum


class GreaterEqualsTen(Minimum):
    __minimum__ = 10


GreaterEqualsTen(11)  # passes
GreaterEqualsTen(10)  # passes
GreaterEqualsTen(9)  # raises valtypes.error.parsing.type.numeric.Minimum
```

## `Positive`

Type for representing a positive `int`. It is a subclass of `Minimum` with `__minimum__` set to `1`.

```python
from valtypes.type.int import Positive

Positive(1)  # passes
Positive(0)  # raises valtypes.error.parsing.type.numeric.Minimum
```

## `NonPositive`

Type for representing a non-positive `int`. It is a subclass of `Maximum` with `__maximum__` set to `0`.

```python
from valtypes.type.int import NonPositive

NonPositive(0)  # passes
NonPositive(1)  # raises valtypes.error.parsing.type.numeric.Maximum
```

## `Negative`

Type for representing a negative `int`. It is a subclass of `Maximum` with `__maximum__` set to `-1`.

```python
from valtypes.type.int import Negative

Negative(-1)  # passes
Negative(0)  # raises valtypes.error.parsing.type.numeric.Maximum
```

## `NonNegative`

Type for representing a non-negative `int`. It is a subclass of `Minimum` with `__minimum__` set to `0`.

```python
from valtypes.type.int import NonNegative

NonNegative(0)  # passes
NonNegative(-1)  # raises valtypes.error.parsing.type.numeric.Minimum
```
