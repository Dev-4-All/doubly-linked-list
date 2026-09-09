from typing import Literal, cast

from node import Node


class DoublyLinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length = 1

    def print_list(self) -> None:
        current = self.head
        while current is not None:
            print(f"{current.value} ", end="")
            current = current.next
        print()

    # TC = O(1)
    def append(self, value: int) -> Literal[True]:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is not None, "List corruption detected: head is set but tail is None"

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

        return True

    # TC = O(1)
    def pop(self) -> Node | None:
        if self.head is None:
            return None

        assert self.tail is not None, "List corruption detected: head is set but tail is None"
        
        temp = self.tail

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            assert self.tail.prev is not None, "List corruption detected: multiple nodes exist but tail.prev is None"

            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1

        return temp 

    # TC = O(1)
    def prepend(self, value: int) -> Literal[True]:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

        return True

    # TC = O(1)
    def pop_start(self) -> Node | None:
        if self.head is None:
            return None

        temp = self.head

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1

        return temp

    # TC = O(n)
    def get(self, index: int) -> Node | None:
        if index < 0 or index >= self.length:
            return None

        temp = self.head

        if index < self.length/2:
            for _ in range(index):
                assert temp is not None, "List length mismatch: encountered None while traversing forward"
                
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                assert temp is not None, "List length mismatch: encountered None while traversing backward"

                temp = temp.prev

        return temp

    # TC = O(n)
    def set_value(self, index: int, value: int) -> bool:
        req_node: Node | None = self.get(index)

        if req_node is not None:
            req_node.value = value
            return True
        
        return False

    # TC = O(n)
    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before: Node = cast(Node, self.get(index-1))
        after = before.next

        assert after is not None, "List corruption detected: after should not be None when inserting in the middle"

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1

        return True

    # TC = O(n)
    def remove(self, index: int) -> Node | None:
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_start()

        if index == self.length-1:
            return self.pop()

        temp: Node = cast(Node, self.get(index))
        before = temp.prev
        after = temp.next

        assert before is not None and after is not None, "List corruption detected: before and after should not be None when removing from the middle"

        temp.prev = None
        temp.next = None
        before.next = after
        after.prev = before

        self.length -= 1

        return temp

    def get_length(self) -> int:
        return self.length
