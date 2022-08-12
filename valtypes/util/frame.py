import sys
from collections.abc import Callable
from types import FrameType, TracebackType
from typing import cast

__all__ = ["get_caller_frame", "get_current_frame_fallback", "get_frame", "get_frame_fallback"]


def get_current_frame_fallback() -> FrameType:
    try:
        raise Exception
    except Exception:
        return cast(FrameType, cast(TracebackType, sys.exc_info()[2]).tb_frame.f_back)


def get_frame_fallback(depth: int) -> FrameType:
    frame = get_current_frame_fallback()
    for _ in range(depth + 1):
        frame = cast(FrameType, frame.f_back)
    return frame


def get_caller_frame() -> FrameType:
    return get_frame(2)


get_frame: Callable[[int], FrameType] = getattr(sys, "_getframe", get_frame_fallback)
