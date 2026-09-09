class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None

    def get_value(self) -> int:
        return self.value
