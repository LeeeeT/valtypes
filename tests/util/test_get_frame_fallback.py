from sys import _getframe as get_frame  # type: ignore

from valtypes.util.frame import get_frame_fallback


def test_returns_the_same_as_sys_get_frame() -> None:
    assert get_frame(0) is get_frame_fallback(0)
    assert get_frame(1) is get_frame_fallback(1)
