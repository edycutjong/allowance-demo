from pocketkit import dedupe, format_duration, parse_duration


def test_hours():
    assert parse_duration("2h") == 7200


def test_format():
    assert format_duration(3725) == "1h 2m 5s"


def test_dedupe_keeps_order():
    assert dedupe([3, 1, 3, 2, 1]) == [3, 1, 2]
