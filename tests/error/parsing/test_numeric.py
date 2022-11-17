from valtypes.error.parsing.numeric import FractionalNumber


def test_fractional_number() -> None:
    assert str(FractionalNumber(1.5)) == "got fractional number: 1.5"
