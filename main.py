from doubly_linked_list import DoublyLinkedList

# create
my_doubly_linked_list = DoublyLinkedList(5)
my_doubly_linked_list.print_list()

print()

# append
my_doubly_linked_list.append(10)
my_doubly_linked_list.print_list()

print()

# pop
print(my_doubly_linked_list.pop().get_value()) # 2 nodes
print(my_doubly_linked_list.pop().get_value()) # 1 node
print(my_doubly_linked_list.pop()) # No nodes

print()

# prepend
my_doubly_linked_list.prepend(10)
my_doubly_linked_list.prepend(5)
my_doubly_linked_list.print_list()

print()

# pop start
print(my_doubly_linked_list.pop_start().get_value())
print(my_doubly_linked_list.pop_start().get_value())
print(my_doubly_linked_list.pop_start())

print()

# None <- 5 <-> 10 <-> 15 <-> 20 <-> 25 -> None
for value in range(5, 26, 5):
    my_doubly_linked_list.append(value)

# get
print(my_doubly_linked_list.get(1).get_value())
print(my_doubly_linked_list.get(3).get_value())

print()

# set
my_doubly_linked_list.set_value(2, 0)
my_doubly_linked_list.print_list()

print()

# insert
my_doubly_linked_list.insert(0, 0)
my_doubly_linked_list.insert(my_doubly_linked_list.get_length(), 0)
my_doubly_linked_list.insert(4, 15)
my_doubly_linked_list.print_list()

print()

# remove
my_doubly_linked_list.remove(0)
my_doubly_linked_list.print_list()
my_doubly_linked_list.remove(my_doubly_linked_list.get_length()-1)
my_doubly_linked_list.print_list()
my_doubly_linked_list.remove(2)
my_doubly_linked_list.print_list()
