<p align="center">
  <img src="https://github.com/LeeeeT/valtypes/blob/main/docs/logo.svg" />
</p>

<p align="center">
    <em>Nothing (almost) should ever be <b>any str</b> or <b>any int</b></em>
</p>

<p align="center">
    <a href="https://pypi.org/project/valtypes">
        <img src="https://img.shields.io/pypi/v/valtypes" />
    </a>
    <a href="https://python.org/downloads">
        <img src="https://img.shields.io/pypi/pyversions/valtypes.svg" />
    </a>
    <a href="https://pepy.tech/project/valtypes">
        <img src="https://img.shields.io/pypi/dm/valtypes" />
    </a>
    <a href="https://github.com/LeeeeT/valtypes/actions/workflows/ci.yml">
        <img src="https://img.shields.io/github/workflow/status/LeeeeT/valtypes/CI" />
    </a>
    <a href="https://valtypes.readthedocs.io/en/latest/?badge=latest">
        <img src="https://img.shields.io/readthedocs/valtypes" />
    </a>
    <a href="https://codecov.io/gh/LeeeeT/valtypes">
        <img src="https://img.shields.io/codecov/c/github/LeeeeT/valtypes" />
    </a>
</p>


---

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/45b4246dde17461ea91bc71b345a956c)](https://app.codacy.com/gh/LeeeeT/valtypes?utm_source=github.com&utm_medium=referral&utm_content=LeeeeT/valtypes&utm_campaign=Badge_Grade_Settings)


## What is Valtypes

**Valtypes** is a flexible data parsing library which will help you make illegal states unrepresentable and enable you to practice ["Parse, don’t validate"][parse-dont-validate] in Python. It has many features that might interest you, so let's dive into some examples.


## Examples

Create constrained types:

```python
from typing import Generic, TypeVar

from valtypes import Constrained


T = TypeVar("T")


class NonEmptyList(Constrained[list[T]], list[T], Generic[T]):
    __constraint__ = bool


def head(l: NonEmptyList[T]) -> T:
    return l[0]


head(NonEmptyList([1, 2, 3]))  # passes
head(NonEmptyList([]))  # runtime error
head([1, 2, 3])  # fails at static type checking
```

Parse complex data structures:

```python
from dataclasses import dataclass, field

from valtypes import parse, Alias
from valtypes.type.numeric import PositiveInt


@dataclass
class User:
    id: PositiveInt = field(metadata=Alias("uid"))
    name: str
    hobbies: NonEmptyList[str]


raw = {"uid": "1", "name": "Fred", "hobbies": ("origami", "curling", 69)}

print(parse(User, raw))
```

```
User(id=1, name='Fred', hobbies=['origami', 'curling', '69'])
```

Get a nice error message if something went wrong:

```python
raw = {"uid": "-1", "hobbies": ()}

print(parse(User, raw))
```

```
valtypes.error.CompositeParsingError: User
├ object 〉 User: not an instance of User
╰ dict[str, object] 〉 User: User
  ├ [id]: PositiveInt
  │ ├ object 〉 PositiveInt: not an instance of PositiveInt
  │ ╰ int 〉 PositiveInt: the value does not match the PositiveInt constraint
  ├ [name]: required field is missing
  ╰ [hobbies]: NonEmptyList[str]
    ├ object 〉 NonEmptyList[str]: not an instance of NonEmptyList[str]
    ╰ list[str] 〉 NonEmptyList[str]: the value does not match the NonEmptyList constraint
```


## Installation

```console
pip install valtypes
```


[parse-dont-validate]: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate
