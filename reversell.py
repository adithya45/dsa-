from singlelinkedlist import *

def reverse(list1):
    list2 = linkl()
    temp = list1.head
    while temp is not None:
        list2.insertf(temp.data)
        temp = temp.next
    return list2


def print_linked_list(linked_list):
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# User interface
linked_list = linkl()

n = int(input("Enter the number of elements: "))
for i in range(n):
    data = int(input("Enter data for node {}: ".format(i + 1)))
    linked_list.insertend(data)

print("Original Linked List:")
print_linked_list(linked_list)

reversed_list = reverse(linked_list)
print("\nReversed Linked List:")
print_linked_list(reversed_list)
