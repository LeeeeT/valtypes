dec_digit = r"[0-9]"

octet = fr"{dec_digit}|[1-9]{dec_digit}|1{dec_digit}{{2}}|2[0-4]{dec_digit}|25[0-5]"

ipv4 = fr"(?<ipv4>{octet}\.{octet}\.{octet}\.{octet})"

hex_digit = r"[0-9A-F]"

hexet = fr"(?<hexet>{hex_digit}{{1,4}})"

zeros_indicator = r"(?<zeros_indicator>::)"

base_ipv6 = (
    fr"(?:{hexet}:){{7}}:{hexet}"
    fr"|{zeros_indicator}(?:{hexet}:){{6}}:{hexet}"
    fr"|{hexet}{zeros_indicator}(?:{hexet}:){{5}}:{hexet}"
    fr"|(?:{hexet}:)?{hexet}{zeros_indicator}(?:{hexet}:){{4}}:{hexet}"
    fr"|(?:{hexet}:){{,2}}{hexet}{zeros_indicator}(?:{hexet}:){{3}}:{hexet}"
    fr"|(?:{hexet}:){{,3}}{hexet}{zeros_indicator}(?:{hexet}:){{2}}:{hexet}"
    fr"|(?:{hexet}:){{,4}}{hexet}{zeros_indicator}{hexet}:{hexet}"
    fr"|(?:{hexet}:){{,5}}{hexet}{zeros_indicator}{hexet}"
    fr"|(?:{hexet}:){{,6}}{hexet}{zeros_indicator}"
)

mixed_ipv6 = (
    fr"(?:{hexet}:){{6}}:{ipv4}"
    fr"|{zeros_indicator}(?:{hexet}:){{5}}:{ipv4}"
    fr"|{hexet}{zeros_indicator}(?:{hexet}:){{4}}:{ipv4}"
    fr"|(?:{hexet}:)?{hexet}{zeros_indicator}(?:{hexet}:){{3}}:{ipv4}"
    fr"|(?:{hexet}:){{,2}}{hexet}{zeros_indicator}(?:{hexet}:){{2}}:{ipv4}"
    fr"|(?:{hexet}:){{,3}}{hexet}{zeros_indicator}{hexet}:{ipv4}"
    fr"|(?:{hexet}:){{,4}}{hexet}{zeros_indicator}{ipv4}"
)

ipv6 = fr"(?<ipv6>{base_ipv6}|{mixed_ipv6})"
