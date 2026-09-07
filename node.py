from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Node | None = None
        self.prev: Node | None = None

    def get_value(self) -> Any:
        return self.value
