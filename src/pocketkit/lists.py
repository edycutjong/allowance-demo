from typing import Iterable, List, Sequence, TypeVar

T = TypeVar("T")


def chunk(items: Sequence[T], size: int) -> List[List[T]]:
    """Split items into lists of `size`; the last list may be shorter."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [list(items[i : i + size]) for i in range(0, len(items) - size + 1, size)]


def dedupe(items: Iterable[T]) -> List[T]:
    """Remove duplicates, keeping the first occurrence and the original order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
