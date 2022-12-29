These types are subclasses of built-in `float` type with some constraints on it.

## `InitHook`

Type with special `__init_hook__` method which is called on instantiation. It can be used to perform some additional checks on the value.

```python
from valtypes.type.float import InitHook
from valtypes.error.parsing import Base as ParsingError


class MultipleOf3(InitHook):
    def __init_hook__(self) -> None:
        if self % 3:
            raise ParsingError(f"{self} is not a multiple of 3")


MultipleOf3(3.)  # passes
MultipleOf3(4.)  # raises ParsingError
```

## `ExclusiveMaximum`

Type for representing a `float` that is less than a given maximum. The maximum allowed value is stored in the `__exclusive_maximum__` attribute.

```python
from valtypes.type.float import ExclusiveMaximum


class LessThanTen(ExclusiveMaximum):
    __exclusive_maximum__ = 10.


LessThanTen(9.9)  # passes
LessThanTen(10.)  # raises valtypes.error.parsing.type.numeric.ExclusiveMaximum
```

## `Maximum`

Type for representing a `float` that is less than or equal to a given maximum. The maximum allowed value is stored in the `__maximum__` attribute.

```python
from valtypes.type.float import Maximum


class LessEqualsTen(Maximum):
    __maximum__ = 10.


LessEqualsTen(9.9)  # passes
LessEqualsTen(10.)  # passes
LessEqualsTen(10.1)  # raises valtypes.error.parsing.type.numeric.Maximum
```

## `ExclusiveMinimum`

Type for representing a `float` that is greater than a given minimum. The minimum allowed value is stored in the `__exclusive_minimum__` attribute.

```python
from valtypes.type.float import ExclusiveMinimum


class GreaterThanTen(ExclusiveMinimum):
    __exclusive_minimum__ = 10.


GreaterThanTen(10.1)  # passes
GreaterThanTen(10.)  # raises valtypes.error.parsing.type.numeric.ExclusiveMinimum
```

## `Minimum`

Type for representing a `float` that is greater than or equal to a given minimum. The minimum allowed value is stored in the `__minimum__` attribute.

```python
from valtypes.type.float import Minimum


class GreaterEqualsTen(Minimum):
    __minimum__ = 10.


GreaterEqualsTen(10.1)  # passes
GreaterEqualsTen(10.)  # passes
GreaterEqualsTen(9.9)  # raises valtypes.error.parsing.type.numeric.Minimum
```

## `Positive`

Type for representing a positive `float`. It is a subclass of `ExclusiveMinimum` with `__exclusive_minimum__` set to `0`.

```python
from valtypes.type.float import Positive

Positive(1.)  # passes
Positive(0.)  # raises valtypes.error.parsing.type.numeric.Minimum
```

## `NonPositive`

Type for representing a non-positive `float`. It is a subclass of `Maximum` with `__maximum__` set to `0`.

```python
from valtypes.type.float import NonPositive

NonPositive(0.)  # passes
NonPositive(1.)  # raises valtypes.error.parsing.type.numeric.Maximum
```

## `Negative`

Type for representing a negative `float`. It is a subclass of `ExclusiveMaximum` with `__exclusive_maximum__` set to `0`.

```python
from valtypes.type.float import Negative

Negative(-1.)  # passes
Negative(0.)  # raises valtypes.error.parsing.type.numeric.Maximum
```

## `NonNegative`

Type for representing a non-negative `float`. It is a subclass of `Minimum` with `__minimum__` set to `0`.

```python
from valtypes.type.float import NonNegative

NonNegative(0.)  # passes
NonNegative(-1.)  # raises valtypes.error.parsing.type.numeric.Minimum
```

## `Portion`

Type for representing a `float` in the range `[0, 1]`. It is a combination of `Minimum` with `__minimum__` set to `0` and `Maximum` with `__maximum__` set to `1`.

```python
from valtypes.type.float import Portion

Portion(0.)  # passes
Portion(1.)  # passes
Portion(-.1)  # raises valtypes.error.parsing.type.numeric.Minimum
Portion(1.1)  # raises valtypes.error.parsing.type.numeric.Maximum
```
