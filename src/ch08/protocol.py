from typing import Protocol, Any

class HasLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

