from valtypes import ForwardRef, parse


def test() -> None:
    """
    It parses a value to the ForwardRef argument
    """

    RecursiveList = list[ForwardRef["int | RecursiveList"]]  # type: ignore

    assert parse(RecursiveList, ("1", ("2", ("3", "4")))) == [1, [2, [3, 4]]]
