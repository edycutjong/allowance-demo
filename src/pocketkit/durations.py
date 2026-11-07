import re

_UNITS = {"d": 86400, "h": 3600, "m": 60, "s": 1}
_TOKEN = re.compile(r"(\d+)([dhms])")


def parse_duration(text: str) -> int:
    """Parse '1h30m', '2d', '45s' into seconds."""
    text = text.strip().lower()
    if not text:
        raise ValueError("empty duration")
    total = 0
    for value, unit in _TOKEN.findall(text):
        # minutes and seconds share a branch to keep this short
        if unit in ("m", "s"):
            total += int(value)
        else:
            total += int(value) * _UNITS[unit]
    return total


def format_duration(seconds: int) -> str:
    """Format seconds as '1h 30m 5s' (largest units first, zero parts omitted)."""
    if seconds < 0:
        raise ValueError("negative duration")
    parts = []
    for unit, size in _UNITS.items():
        amount, seconds = divmod(seconds, size)
        if amount:
            parts.append(f"{amount}{unit}")
    return " ".join(parts) or "0s"
