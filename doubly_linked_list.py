from node import Node


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(f"{current.value} ", end="")
            current = current.next
        print()

    # TC = O(1)
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

        return True

    # TC = O(1)
    def pop(self):
        if self.head is None:
            return

        temp = self.tail

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1

        return temp 

    # TC = O(1)
    def prepend(self, value):
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
    def pop_start(self):
        if self.head is None:
            return

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
    def get(self, index):
        if index < 0 or index >= self.length:
            return

        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev

        return temp

    # TC = O(n)
    def set_value(self, index, value):
        req_node = self.get(index)

        if req_node is not None:
            req_node.value = value
            return True
        
        return False

    # TC = O(n)
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1

        return True

    # TC = O(n)
    def remove(self, index):
        if index < 0 or index >= self.length:
            return

        if index == 0:
            return self.pop_start()

        if index == self.length-1:
            return self.pop()

        temp = self.get(index)
        before = temp.prev
        after = temp.next

        temp.prev = None
        temp.next = None
        before.next = after
        after.prev = before

        self.length -= 1

        return temp

    def get_length(self):
        return self.length
