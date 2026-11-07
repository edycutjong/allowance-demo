from datetime import date, timedelta


def business_days_between(start: date, end: date) -> int:
    """Count Monday-Friday days from start to end, both inclusive."""
    if end < start:
        start, end = end, start
    days = 0
    current = start
    while current < end:
        if current.weekday() < 5:
            days += 1
        current += timedelta(days=1)
    return days
