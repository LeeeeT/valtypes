from valtypes.condition import variable_length_tuple_alias


def test_returns_true_if_value_is_variable_length_tuple_alias() -> None:
    assert variable_length_tuple_alias.check(tuple[int, ...])


def test_returns_false_if_value_is_fixed_length_tuple_alias() -> None:
    assert not variable_length_tuple_alias.check(tuple[int, int])
