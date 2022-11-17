## Dataclasses

`dict` can be parsed into dataclass according to the following rules:

  * `dict` must contain all required fields of the dataclass. Otherwise, an error will be raised.

    ```python
    from dataclasses import dataclass

    from valtypes import parse_json


    @dataclass
    class Foo:
        a: int
        b: str


    parse_json(Foo, {"a": 1, "b": "2"})  # Foo(a=1, b='2')

    parse_json(Foo, {"a": 1})  # raises exception group with valtypes.error.parsing.dataclass.MissingField
    ```

  * `dict` values are parsed to the corresponding field types. If parsing fails, an error will be raised.

    ```python
    from dataclasses import dataclass

    from valtypes import parse_json


    @dataclass
    class Foo:
        a: int
        b: str


    parse_json(Foo, {"a": 1, "b": "2"})  # Foo(a=1, b='2')

    parse_json(Foo, {"a": 1, "b": 2})  # raises exception group with valtypes.error.parsing.WrongType
    ```

  * `dict` might not contain optional fields (those that have a default or a default factory). In this case, the default (or default factory) will be used.

    ```python
    from dataclasses import dataclass, field

    from valtypes import parse_json


    @dataclass
    class Foo:
        a: int = field(default_factory=int)
        b: int = field(default=1)
        c: int = 2


    parse_json(Foo, {"a": 3, "c": 5})  # Foo(a=3, b=1, c=5)

    parse_json(Foo, {"b": 4})  # Foo(a=0, b=4, c=2)
    ```

  * `dict` doesn't have to contain fields that are not included to the `__init__` method.

    ```python
    from dataclasses import dataclass, field

    from valtypes import parse_json


    @dataclass
    class Foo:
        a: int = field(init=False, default=1)
        b: int


    parse_json(Foo, {"b": 2})  # Foo(a=1, b=2)

    parse_json(Foo, {"a": 0, "b": 2})  # Foo(a=1, b=2)
    ```

  * If the dataclass doesn't have a `__init__` method at all, an error will be raised.

    ```python
    from dataclasses import dataclass

    from valtypes import parse_json


    @dataclass(init=False)
    class Foo:
        a: int
        b: int


    parse_json(Foo, {"a": 1, "b": 2})  # raises valtypes.error.parsing.NoParser
    ```

  * `dict` doesn't have to contain `ClassVar` fields.

    ```python
    from typing import ClassVar
    from dataclasses import dataclass

    from valtypes import parse_json


    @dataclass
    class Foo:
        a: ClassVar[int]
        b: int


    parse_json(Foo, {"b": 2})  # Foo(b=2)
    ```

  * `dict` must contain `InitVar` fields.

    ```python
    from dataclasses import dataclass, InitVar

    from valtypes import parse_json


    @dataclass
    class Foo:
        a: InitVar[int]
        b: int

        def __post_init__(self, a: int) -> None:
            self._a = a


    parse_json(Foo, {"a": 1, "b": 2})  # Foo(b=2)

    parse_json(Foo, {"b": 2})  # raises exception group with valtypes.error.parsing.dataclass.MissingField
    ```

  * `dict` can contain fields that are not defined in the dataclass. They will be ignored.

Valtypes doesn't stop parsing after the first error. It collects all errors and raises them as an exception group.

```python
from dataclasses import dataclass

from valtypes import parse_json


@dataclass
class Foo:
    a: int
    b: str
    c: str


parse_json(Foo, {"a": "1", "c": 3})
```

```
| valtypes.error.parsing.dataclass.Composite: dataclass parsing error (3 sub-exceptions)
+-+---------------- 1 ----------------
  | valtypes.error.parsing.dataclass.WrongFieldValue: can't parse field 'a' (1 sub-exception)
  +-+---------------- 1 ----------------
    | valtypes.error.parsing.generic.WrongType: not an instance of int
    +------------------------------------
  +---------------- 2 ----------------
  | valtypes.error.parsing.dataclass.MissingField: required field 'b' is missing
  +---------------- 3 ----------------
  | valtypes.error.parsing.dataclass.WrongFieldValue: can't parse field 'c' (1 sub-exception)
  +-+---------------- 1 ----------------
    | valtypes.error.parsing.generic.WrongType: not an instance of str
    +------------------------------------
```

*(Traceback omitted)*

## Built-in types

When trying to parse a value to some built-in type (`int`, `float`, `str`, `bytes`, `bytearray` or `object`), valtypes checks if the value is an instance of that type. And if it is, the value will be returned as is. Otherwise, an error will be raised.

```python
from valtypes import parse_json

parse_json(int, 1)  # 1
parse_json(int, "1")  # raises valtypes.error.parsing.generic.WrongType
```

## Subclasses of built-in types

When trying to parse a value to subclass of a built-in type (`int`, `float`, `str`, `bytes` or `bytearray`), valtypes first tries to parse the value to the base type and then passes the result to the constructor of the original type to get an instance of it.

```python
from valtypes import parse_json


class Foo(int):
    pass


parse_json(Foo, 1)  # Foo(1)
parse_json(Foo, "1")  # raises valtypes.error.parsing.generic.WrongType
```

## Built-in generic types

When trying to parse a value to some built-in generic type (`list`, `tuple`, `set`, `frozenset` or `dict`), valtypes checks if the value is an instance of that type, then it parses all the elements to the type specified in the generic arguments. If the value is not an instance of that type or parsing of some element fails, an error will be raised.

```python
from valtypes import parse_json

parse_json(list[int], [1, 2, 3])  # [1, 2, 3]
parse_json(list[int], [1, "2", 3])  # raises exception group with valtypes.error.parsing.generic.WrongType
```

Valtypes doesn't stop parsing after the first error. It collects all errors and raises them as an exception group.

```python
from valtypes import parse_json

parse_json(list[float], [True, 2., "3"])
```

```
| valtypes.error.parsing.sequence.Composite: sequence parsing error (2 sub-exceptions)
+-+---------------- 1 ----------------
  | valtypes.error.parsing.sequence.WrongItem: can't parse item at index 0 (1 sub-exception)
  +-+---------------- 1 ----------------
    | valtypes.error.parsing.generic.WrongType: not an instance of float
    +------------------------------------
  +---------------- 2 ----------------
  | valtypes.error.parsing.sequence.WrongItem: can't parse item at index 2 (1 sub-exception)
  +-+---------------- 1 ----------------
    | valtypes.error.parsing.generic.WrongType: not an instance of float
    +------------------------------------
```

*(Traceback omitted)*
