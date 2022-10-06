<p align="center">
  <img src="https://raw.githubusercontent.com/LeeeeT/valtypes/main/docs/logo.svg" />
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

## What is valtypes

**Valtypes** is a flexible data parsing library which will help you make illegal states unrepresentable and enable you to practice ["Parse, don’t validate"][parse-dont-validate] in Python. It has many features that might interest you, so let's dive into some examples.

## Examples

Create constrained types:

```python
from valtypes.type.str import NonEmpty, MaximumLength

class Name(NonEmpty, MaximumLength):
    __maximum_length__ = 20

def initials(name: Name) -> str:
    # name is guaranteed to be a non-empty string of maximum length 20
    return f"{name[0]}."

initials(Name("Fred"))  # passes
initials(Name(""))  # parsing error
initials("")  # fails at static type checking
```

Parse complex data structures:

```python
from dataclasses import dataclass

from valtypes import parse
from valtypes.type import int, list, str

@dataclass
class User:
    id: int.Positive
    name: Name
    hobbies: list.NonEmpty[str.NonEmpty]

raw = {"id": 1, "name": "Fred", "hobbies": ["origami", "curling", "programming"]}

print(parse(User, raw))
```

```
User(id=1, name='Fred', hobbies=['origami', 'curling', 'programming'])
```

## Installation

```console
pip install valtypes
```

[parse-dont-validate]: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate
