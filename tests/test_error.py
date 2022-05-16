from valtypes.error import (
    BaseParsingError,
    CompositeParsingError,
    ConstraintError,
    ConversionError,
    FractionalNumberError,
    MissingFieldError,
    NoParserError,
    NotEnoughItemsError,
    ParsingError,
    RecursiveParsingError,
    WrongFieldError,
    WrongItemError,
    WrongTypeError,
)
from valtypes.type.numeric import Portion


def test_no_parser_error() -> None:
    error = NoParserError(..., list[int])
    assert str(error) == "there's no parser for list[int]"


def test_parsing_error() -> None:
    error = ParsingError(list[int], tuple[int], BaseParsingError("cause"))
    assert str(error) == "list[int] 〉 tuple[int]: cause"


def test_recursive_parsing_error() -> None:
    error = RecursiveParsingError((object, list[int], int))
    assert str(error) == "recursion detected: object 〉 list[int] 〉 int"


def test_composite_parsing_error() -> None:
    error = CompositeParsingError(
        int | str,
        (
            CompositeParsingError(int, (BaseParsingError("cause 1"), BaseParsingError("cause 2"))),
            CompositeParsingError(str, (BaseParsingError("cause 3"), BaseParsingError("cause 4"))),
        ),
    )
    assert str(error) == "int | str\n├ int\n│ ├ cause 1\n│ ╰ cause 2\n╰ str\n  ├ cause 3\n  ╰ cause 4"


def test_wrong_type_error() -> None:
    error = WrongTypeError(..., "type")
    assert str(error) == "not an instance of 'type'"


def test_conversion_error() -> None:
    error = ConversionError(..., tuple[bytes])
    assert str(error) == "can't convert the value to tuple[bytes]"


def test_constraint_error() -> None:
    error = ConstraintError(..., Portion)
    assert str(error) == f"the value doesn't match the {Portion.__name__} constraint"


def test_fractional_number_error() -> None:
    error = FractionalNumberError(0)
    assert str(error) == "fractional number"


def test_wrong_item_error() -> None:
    error = WrongItemError(42, BaseParsingError("cause"))
    assert str(error) == "[42]: cause"


def test_not_enough_items_error_single() -> None:
    error = NotEnoughItemsError(1)
    assert str(error) == "1 item is missing"


def test_not_enough_items_error_many() -> None:
    error = NotEnoughItemsError(3)
    assert str(error) == "3 items are missing"


def test_wrong_field_error() -> None:
    error = WrongFieldError("field", BaseParsingError("cause"))
    assert str(error) == "[field]: cause"


def test_missing_field_error() -> None:
    error = MissingFieldError("field")
    assert str(error) == "[field]: required field is missing"
