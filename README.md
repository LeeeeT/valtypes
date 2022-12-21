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
    <img src="https://img.shields.io/github/checks-status/LeeeeT/valtypes/main" />
    <a href="https://valtypes.readthedocs.io/en/latest/?badge=latest">
        <img src="https://img.shields.io/readthedocs/valtypes" />
    </a>
</p>

---

**Documentation**: [valtypes.readthedocs.io][docs]

**Source code**: [github.com/LeeeeT/valtypes][source]

---

## What is valtypes

**Valtypes** is a flexible data parsing library which will help you make illegal states unrepresentable and enable you to practice ["Parse, don’t validate"](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate) in Python. It has many features that might interest you, so let's dive into some examples.

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

from valtypes import parse_json
from valtypes.type import int, list, str


@dataclass
class User:
    id: int.Positive
    name: Name
    hobbies: list.NonEmpty[str.NonEmpty]


raw = {"id": 1, "name": "Fred", "hobbies": ["origami", "curling", "programming"]}

print(parse_json(User, raw))
```

```
User(id=1, name='Fred', hobbies=['origami', 'curling', 'programming'])
```

Get a nice error message if something went wrong (traceback omitted):

```python
raw = {"id": 0, "hobbies": [""]}

parse_json(User, raw)
```

```
| valtypes.error.parsing.dataclass.Composite: dataclass parsing error (3 sub-exceptions)
+-+---------------- 1 ----------------
  | valtypes.error.parsing.dataclass.WrongFieldValue: can't parse field 'id' (1 sub-exception)
  +-+---------------- 1 ----------------
    | valtypes.error.parsing.type.numeric.Minimum: the value must be greater than or equal to 1, got: 0
    +------------------------------------
  +---------------- 2 ----------------
  | valtypes.error.parsing.dataclass.MissingField: required field 'name' is missing
  +---------------- 3 ----------------
  | valtypes.error.parsing.dataclass.WrongFieldValue: can't parse field 'hobbies' (1 sub-exception)
  +-+---------------- 1 ----------------
    | valtypes.error.parsing.sequence.Composite: sequence parsing error (1 sub-exception)
    +-+---------------- 1 ----------------
      | valtypes.error.parsing.sequence.WrongItem: can't parse item at index 0 (1 sub-exception)
      +-+---------------- 1 ----------------
        | valtypes.error.parsing.type.sized.MinimumLength: length 0 is less than the allowed minimum of 1
        +------------------------------------
```

## Installation

Install from [PyPI]:

```console
pip install valtypes
```

Build the latest version from [source]:

```console
pip install git+https://github.com/LeeeeT/valtypes
```

[docs]: https://valtypes.readthedocs.io

[source]: https://github.com/LeeeeT/valtypes

[PyPI]: https://pypi.org/project/valtypes
