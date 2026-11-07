# pocketkit

Small helpers for durations, dates and lists.

```bash
pip install git+https://github.com/edycutjong/allowance-demo
```

```python
from pocketkit import parse_duration, business_days_between, chunk
parse_duration("1h30m")                     # seconds
business_days_between(date(2026, 11, 2), date(2026, 11, 6))   # Mon..Fri, inclusive
chunk([1, 2, 3, 4, 5], 2)                   # [[1, 2], [3, 4], [5]]
```

## Contributing

Found a bug? Open an issue with steps to reproduce. This repo uses
[Allowance](https://allowance.edycu.dev): comment `/repro` on your issue and the bot will try to
reproduce it in a sandbox on your own daily allowance.
