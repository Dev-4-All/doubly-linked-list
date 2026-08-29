from doubly_linked_list import DoublyLinkedList

# create
my_doubly_linked_list = DoublyLinkedList(5)
my_doubly_linked_list.print_list()

# append
my_doubly_linked_list.append(10)
my_doubly_linked_list.print_list()

# pop
print(my_doubly_linked_list.pop().get_value()) # 2 nodes
print(my_doubly_linked_list.pop().get_value()) # 1 node
print(my_doubly_linked_list.pop()) # No nodes
