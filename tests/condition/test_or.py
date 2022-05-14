from valtypes.condition import false, true


def test_all_return_false() -> None:
    """
    It returns False if all the conditions return False
    """

    assert not (false | false)(...)


def test_some_return_true() -> None:
    """
    It returns True if any condition returns True
    """

    assert (false | true)(...)
    assert (true | true)(...)
