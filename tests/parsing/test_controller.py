import pytest

from valtypes.condition import Is
from valtypes.error import CompositeParsingError, ConversionError, NoParserError, ParsingError, RecursiveParsingError
from valtypes.parsing import Collection, Controller, Rule, with_source_type
from valtypes.parsing.parser import FromCallable


def test_no_parser() -> None:
    """
    It raises an error if there's no parsers in the collection matching the desired type
    """

    collection = Collection([Rule(FromCallable(str), Is(str))])

    with pytest.raises(NoParserError) as info:
        collection.parse(int, ...)

    assert info.value == NoParserError(..., int)


def test_recursion() -> None:
    """
    It raises an error when parsers try calling each other recursively
    """

    collection = Collection()

    @collection.register(Is(int))
    @with_source_type(str)
    def str_to_int(target_type: type[int], source: str, controller: Controller) -> int:
        return 0

    @collection.register(Is(str))
    @with_source_type(int)
    def int_to_str(target_type: type[str], source: int, controller: Controller) -> str:
        return ""

    with pytest.raises(CompositeParsingError) as info:
        collection.parse(int, ...)

    assert info.value == CompositeParsingError(
        int,
        (
            ParsingError(
                str,
                int,
                CompositeParsingError(
                    str,
                    (
                        ParsingError(
                            int,
                            str,
                            RecursiveParsingError((int, str)),
                        ),
                    ),
                ),
            ),
        ),
    )


def test_multiple_matching_parsers_with_different_source_types() -> None:
    """
    It properly constructs a parsing error when there are multiple parsers for a target type with different source types
    """

    collection = Collection()

    @collection.register(Is(int))
    @with_source_type(str)
    def to_int_1(target_type: type[int], source: str, controller: Controller) -> int:
        return 0

    @collection.register(Is(int))
    def to_int_2(target_type: type[int], source: object, controller: Controller) -> int:
        raise ConversionError(source, int)

    with pytest.raises(CompositeParsingError) as info:
        collection.parse(int, ...)

    assert info.value == CompositeParsingError(
        int,
        (ParsingError(str, int, NoParserError(..., str)), ParsingError(object, int, ConversionError(..., int))),
    )
