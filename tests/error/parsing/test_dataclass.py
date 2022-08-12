import valtypes.error.parsing.dataclass as dataclass_parsing_error
from valtypes import error


def test_wrong_field_value() -> None:
    e = dataclass_parsing_error.WrongFieldValue("field", error.Base("cause"))
    assert str(e) == "[field]: cause"


def test_missing_field() -> None:
    e = dataclass_parsing_error.MissingField("field")
    assert str(e) == "[field]: required field is missing"
