import valtypes.error.parsing.numeric as error


def test_fractional_number() -> None:
    e = error.FractionalNumber(1.5)
    assert str(e) == "got fractional number: 1.5"
