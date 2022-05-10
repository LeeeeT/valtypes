from valtypes.condition import false, true


def test() -> None:
    """
    It inverts the condition
    """

    assert not (~true)(...)
    assert (~false)(...)
