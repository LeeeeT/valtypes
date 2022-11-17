These types are mixins that are used to create other constrained types.

## `InitHook`

Type with special `__init_hook__` method which is called on instantiation. It can be used to perform some additional checks on the value.

```python
from valtypes.type.generic import InitHook
from valtypes.error.parsing import Base as ParsingError


class Contains42(InitHook, list[int]):
    def __init_hook__(self) -> None:
        if 42 not in self:
            raise ParsingError(f"{self} doesn't contain 42")


Contains42([41, 42, 43])  # passes
Contains42([1, 2, 3])  # raises ParsingError
```
