from typing import Any, ClassVar, Final

from valtypes.parsing import collection
from valtypes.parsing.parser import object_to_special_form


def test_simple() -> None:
    assert object_to_special_form.parse(ClassVar, 12, collection) == 12
    assert object_to_special_form.parse(Final, "foo", collection) == "foo"
    object_to_special_form.parse(Any, object(), collection)
