from collections.abc import Iterable

from regex import Match

from valtypes.type.network import Hexet, IPv4, IPv6

from .from_callable import FromCallable
from .str_to_ipv4 import str_to_ipv4

__all__ = ["Parser", "match_to_ipv6"]


@FromCallable
def match_to_ipv6(match: Match[str]) -> IPv6:
    return Parser(match).parse()


class Parser:
    def __init__(self, match: Match[str]):
        self._match = match

    def parse(self) -> IPv6:
        return IPv6(*self._hexets_before_elision, *self._elided_zero_valued_hexets, *self._hexets_after_elision, *self._ipv4_hexets)

    @property
    def _hexets_before_elision(self) -> list[Hexet]:
        return [Hexet(raw_hexet) for raw_hexet in self._raw_hexets_before_elision]

    @property
    def _raw_hexets_before_elision(self) -> list[str]:
        return self._raw_hexets[: self._elision_hexet_index]

    @property
    def _elided_zero_valued_hexets(self) -> list[Hexet]:
        return [Hexet(0)] * self._elided_hexets_count

    @property
    def _hexets_after_elision(self) -> list[Hexet]:
        return [Hexet(raw_hexet) for raw_hexet in self._raw_hexets_after_elision]

    @property
    def _raw_hexets_after_elision(self) -> list[str]:
        return self._raw_hexets[self._elision_hexet_index :]

    @property
    def _elision_hexet_index(self) -> int:
        for hexet_index, hexet_end_position in enumerate(self._hexets_end_positions):
            if hexet_end_position == self._elision_start_position:
                return hexet_index + 1
        return 0

    @property
    def _hexets_end_positions(self) -> list[int]:
        return [span[1] for span in self._match.spans("hexet")]

    @property
    def _elision_start_position(self) -> int:
        return self._match.span("elision")[0]

    @property
    def _elided_hexets_count(self) -> int:
        return self._target_hexets_count - len(self._raw_hexets)

    @property
    def _target_hexets_count(self) -> int:
        return 6 if self._has_ipv4 else 8

    @property
    def _raw_hexets(self) -> list[str]:
        return self._match.captures("hexet")

    @property
    def _ipv4_hexets(self) -> Iterable[Hexet]:
        return self._ipv4.hexets if self._has_ipv4 else ()

    @property
    def _has_ipv4(self) -> bool:
        return bool(self._match["ipv4"])

    @property
    def _ipv4(self) -> IPv4:
        return str_to_ipv4.parse(self._raw_ipv4)

    @property
    def _raw_ipv4(self) -> str:
        return self._match["ipv4"]
