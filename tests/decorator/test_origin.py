from valtypes.decorator import origin


def test_returns_generic_alias_origin() -> None:
    assert origin.decorate(list[int]) is list
    assert origin.decorate(tuple[str, ...]) is tuple
