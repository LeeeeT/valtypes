__all__ = [
    "absolute_or_empty_path",
    "absolute_path",
    "fragment",
    "ipv4",
    "ipv6",
    "ipvfuture_content",
    "no_scheme_path",
    "query",
    "reg_name",
    "rootless_path",
    "scheme",
    "user_info",
]


octet = r"(?P<octet>\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])"

ipv4 = rf"(?P<ipv4>{octet}\.{octet}\.{octet}\.{octet})"

hexadecimal_digit = r"[0-9A-Fa-f]"

hexet = rf"(?P<hexet>{hexadecimal_digit}{{1,4}})"

last_32_bits = rf"(?:{hexet}:{hexet}|{ipv4})"

elision = r"(?P<elision>::)"

ipv6 = (
    rf"(?:"
    rf"(?:{hexet}:){{6}}{last_32_bits}"
    rf"|(?:{elision}(?:{hexet}:){{5}}{last_32_bits})"
    rf"|{hexet}?{elision}(?:{hexet}:){{4}}{last_32_bits}"
    rf"|(?:(?:{hexet}:)?{hexet})?{elision}(?:{hexet}:){{3}}{last_32_bits}"
    rf"|(?:(?:{hexet}:){{0,2}}{hexet})?{elision}(?:{hexet}:){{2}}{last_32_bits}"
    rf"|(?:(?:{hexet}:){{0,3}}{hexet})?{elision}{hexet}:{last_32_bits}"
    rf"|(?:(?:{hexet}:){{0,4}}{hexet})?{elision}{last_32_bits}"
    rf"|(?:(?:{hexet}:){{0,5}}{hexet})?{elision}{hexet}"
    rf"|(?:(?:{hexet}:){{0,6}}{hexet})?{elision}"
    rf")"
)

unreserved = r"(?:[0-9A-Fa-z-._~])"

pct_encoded = rf"(?:%{hexadecimal_digit}{hexadecimal_digit})"

sub_delims = r"(?:[!$&'()*+,;=])"

pchar = rf"(?:{unreserved}|{pct_encoded}|{sub_delims}|:|@)"

ipvfuture_content = rf"(?:(?:{unreserved}|{sub_delims}|:)+)"

ipvfuture = rf"(?:[Vv]{hexadecimal_digit}+\.{ipvfuture_content})"

scheme = r"(?:[A-Za-z](?:[A-Za-z]|\d|\+|-|\.)*)"

user_info = rf"(?:(?:{unreserved}|{pct_encoded}|{sub_delims}|:)*)"

ip_literal = rf"(?:\[(?:{ipv6}|{ipvfuture})\])"

reg_name = rf"(?:(?:{unreserved}|{pct_encoded}|{sub_delims})*)"

host = rf"(?:{ip_literal}|{ipv4}|{reg_name})"

port = r"(?:\d*)"

authority = rf"(?:(?:{user_info}@)?{host}(?::{port})?)"

segment = rf"(?:{pchar}*)"

non_empty_segment = rf"(?:{pchar}+)"

non_empty_no_colon_segment = rf"(?:(?:{unreserved}|{pct_encoded}|{sub_delims}|@)+)"

absolute_or_empty_path = rf"(?:(?:/{segment})*)"

absolute_path = rf"(?:/(?:{non_empty_segment}(?:/{segment})*)?)"

no_scheme_path = rf"(?:{non_empty_no_colon_segment}(?:/{segment})*)"

rootless_path = rf"(?:{non_empty_segment}(?:/{segment})*)"

empty_path = r"(?:)"

query = rf"(?:(?:{pchar}|/|\?)*)"

fragment = rf"(?:(?:{pchar}|/|\?)*)"

hier_part = rf"(?://{authority}{absolute_or_empty_path}|{absolute_path}|{rootless_path}|{empty_path})"

relative_part = rf"(?://{authority}{absolute_or_empty_path}|{absolute_path}|{no_scheme_path}|{empty_path})"

absolute_uri = rf"(?:{scheme}:{hier_part}(?:\?{query})?)"

uri = rf"(?:{scheme}:{hier_part}(?:\?{query})?(?:#{fragment})?)"

relative_reference = rf"(?:{relative_part}(?:\?{query})?(?:#{fragment})?)"

uri_reference = rf"(?:{uri}|{relative_reference})"
