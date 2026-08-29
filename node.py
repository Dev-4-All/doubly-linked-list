class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def get_value(self):
        return self.value
