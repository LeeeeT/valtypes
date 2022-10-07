import valtypes.error.parsing as error


def test_wrong_type() -> None:
    e = error.WrongType(..., "type")
    assert str(e) == "not an instance of 'type'"


def test_composite() -> None:
    e = error.Composite(
        (
            error.WrongType(..., int),
            error.Composite(
                (
                    error.Base("nested cause 1"),
                    error.Base("nested cause 2"),
                ),
            ),
            error.WrongType(..., list[str]),
        )
    )
    assert str(e) == (
        "composite error"
        "\n├ not an instance of int"
        "\n├ composite error"
        "\n│ ├ nested cause 1"
        "\n│ ╰ nested cause 2"
        "\n╰ not an instance of list[str]"
    )
