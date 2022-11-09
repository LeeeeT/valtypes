These abstract types are mixins that are used to create constrained sized types.

## `LengthHook`

Type with special `__length_hook__` method which is called whenever the length of an object is going to change.

Implementation methods that are changing the length of an object should call this hook with the new length that the object would have after the operation.

```python
from typing import Generic, TypeVar
from collections.abc import Iterable

from valtypes.type.sized import LengthHook
from valtypes.error.parsing import Base as ParsingError


T = TypeVar("T")


class MyList(LengthHook, Generic[T]):
    def __init__(self, items: Iterable[T]):
        self._items = list(items)
        super().__init__()
    
    def add(self, item: T) -> None:
        self.__length_hook__(len(self) + 1)
        self._items.append(item)

    def __len__(self) -> int:
        return len(self._items)


class MyListWithEvenLength(MyList[T]):
    def __length_hook__(self, new_length: int) -> None:
        if new_length % 2:
            raise ParsingError(f"{self.__class__.__name__} can't have odd length")


l = MyListWithEvenLength([1, 2])  # passes
l.add(3)  # raises ParsingError
```

There are also some shortcuts for common cases:

* `__notify_length_delta__`: takes the delta of the length and calls `__length_hook__` with the current length + delta.
* `__notify_length_increments__`: calls `__length_hook__` with the current length + 1.
* `__notify_length_decrements__`: calls `__length_hook__` with the current length - 1.

So, `MyList` can be rewritten as:

```python hl_lines="7"
class MyList(LengthHook, Generic[T]):
    def __init__(self, items: Iterable[T]):
        self._items = list(items)
        super().__init__()
    
    def add(self, item: T) -> None:
        self.__notify_length_increments__()
        self._items.append(item)

    def __len__(self) -> int:
        return len(self._items)
```

## `MinimumLength`

Type for representing an object that has a given minimum length. The minimum allowed length is stored in the `__minimum_length__` attribute.

Example of creating a new abstract class and combining it with previously created `MyList` class:

```python
from abc import ABC

from valtypes.type.sized import MinimumLength


class AtLeastTwoElements(MinimumLength, ABC):
    __minimum_length__ = 2


class MyListWithAtLeastTwoElements(MyList[T], AtLeastTwoElements):
    pass


MyListWithAtLeastTwoElements([1, 2])  # passes
MyListWithAtLeastTwoElements([1])  # raises valtypes.error.parsing.type.sized.MinimumLength
```

## `MaximumLength`

Type for representing an object that has a given maximum length. The maximum allowed length is stored in the `__maximum_length__` attribute.

Example of creating a new abstract class and combining it with previously created `MyList` class:

```python
from abc import ABC

from valtypes.type.sized import MaximumLength


class AtMostTwoElements(MaximumLength, ABC):
    __maximum_length__ = 2


class MyListWithAtMostTwoElements(MyList[T], AtMostTwoElements):
    pass


MyListWithAtMostTwoElements([1, 2])  # passes
MyListWithAtMostTwoElements([1, 2, 3])  # raises valtypes.error.parsing.type.sized.MaximumLength
```
