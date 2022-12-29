These types are subclasses of built-in `str` type with some constraints on it.

## `InitHook`

Type with special `__init_hook__` method which is called on instantiation. It can be used to perform some additional checks on the value.

```python
from valtypes.type.str import InitHook
from valtypes.error.parsing import Base as ParsingError


class Uppercase(InitHook):
    def __init_hook__(self) -> None:
        if not self.isupper():
            raise ParsingError(f"{self!r} is not uppercase")


Uppercase("FOO")  # passes
Uppercase("foo")  # raises ParsingError
```

## `MinimumLength`

Type for representing a `str` that has a given minimum length. The minimum allowed length is stored in the `__minimum_length__` attribute.

```python
from valtypes.type.str import MinimumLength


class AtLeastTwoChars(MinimumLength):
    __minimum_length__ = 2


AtLeastTwoChars("foo")  # passes
AtLeastTwoChars("f")  # raises valtypes.error.parsing.type.sized.MinimumLength
```

## `MaximumLength`

Type for representing a `str` that has a given maximum length. The maximum allowed length is stored in the `__maximum_length__` attribute.

```python
from valtypes.type.str import MaximumLength


class AtMostTwoChars(MaximumLength):
    __maximum_length__ = 2


AtMostTwoChars("foo")  # passes
AtMostTwoChars("fooo")  # raises valtypes.error.parsing.type.sized.MaximumLength
```

## `NonEmpty`

Type for representing a non-empty `str`. It is a subclass of `MinimumLength` with `__minimum_length__` set to `1`.

```python
from valtypes.type.str import NonEmpty

NonEmpty("foo")  # passes
NonEmpty()  # raises valtypes.error.parsing.type.sized.MinimumLength
```

## `RePattern`

Type for representing a `str` that fully matches a given regular expression. The regular expression is stored in the `__pattern__` attribute.

```python
import re

from valtypes.type.str import RePattern


class Numeric(RePattern):
    __pattern__ = re.compile(r"\d+")


Numeric("123")  # passes
Numeric("foo")  # raises valtypes.error.parsing.type.str.Pattern
```
