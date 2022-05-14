from valtypes.condition import is_variable_length_tuple


def test_not_generic_alias() -> None:
    """
    It returns False if the value isn't a generic alias
    """

    assert not is_variable_length_tuple(...)


def test_origin_is_not_tuple() -> None:
    """
    It returns False if the origin isn't a tuple
    """

    assert not is_variable_length_tuple(list[int])


def test_fixed_length_tuple() -> None:
    """
    It returns False if the value is a generic alias of a fixed-length tuple
    """

    assert not is_variable_length_tuple(tuple[int])
    assert not is_variable_length_tuple(tuple[int, int])  # type: ignore


def test_variable_length_tuple() -> None:
    """
    It returns True if the value is a generic alias of a variable-length tuple
    """

    assert is_variable_length_tuple(tuple[int, ...])
