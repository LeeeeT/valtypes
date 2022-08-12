import valtypes.error.parsing as parsing_error


def test_no_parser() -> None:
    e = parsing_error.NoParser(list[int])
    assert str(e) == "there's no parser for list[int]"


def test_recursion() -> None:
    e = parsing_error.Recursion((object, list[int], int))
    assert str(e) == "recursion detected: object › list[int] › int"


def test_wrong_type() -> None:
    e = parsing_error.WrongType(..., "type")
    assert str(e) == "not an instance of 'type'"


def test_parsing() -> None:
    e = parsing_error.Parsing("123")
    assert str(e) == "can't parse the value '123'"


def test_composite() -> None:
    e = parsing_error.Composite(
        (
            parsing_error.NoParser(list[int]),
            parsing_error.Composite(
                (
                    parsing_error.Recursion((object, list[int], int)),
                    parsing_error.Parsing("123"),
                ),
            ),
            parsing_error.Parsing(456),
        )
    )
    assert str(e) == (
        "composite error"
        "\n├ there's no parser for list[int]"
        "\n├ composite error"
        "\n│ ├ recursion detected: object › list[int] › int"
        "\n│ ╰ can't parse the value '123'"
        "\n╰ can't parse the value 456"
    )
