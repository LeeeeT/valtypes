.. image:: docs/logo.svg
    :align: center


*Nothing (almost) should ever be* **any str** *or* **any int**


.. image:: https://img.shields.io/pypi/v/valtypes.svg
    :target: https://pypi.org/project/valtypes

.. image:: https://img.shields.io/pypi/pyversions/valtypes.svg
    :target: https://python.org/downloads

.. image:: https://pepy.tech/badge/valtypes/month
    :target: https://pepy.tech/project/valtypes


=========


What is Valtypes
----------------

**Valtypes** is a flexible data parsing library which will help you make illegal states
unrepresentable and enable you to practice `"Parse, don’t validate"
<https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate>`_ in Python.
It has many features that might interest you, so let's dive into some examples.


Examples
--------

Creating constrained types:

.. code-block:: python

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

Complex parsing:

.. code-block:: python

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

::

    User(id=1, name='Fred', hobbies=['origami', 'curling', '69'])

Get a nice error message if something went wrong:

.. code-block:: python

    raw = {"uid": "-1", "hobbies": ()}

    print(parse(User, raw))

::

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



Installation
------------

::

    pip install valtypes
