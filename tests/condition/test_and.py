from valtypes.condition import false, true


def test_some_returns_false() -> None:
    """
    It returns False if some condition returns False
    """

    assert not (false & false)(...)
    assert not (true & false)(...)


def test_all_return_true() -> None:
    """
    It returns True if all conditions return True
    """

    assert (true & true)(...)
