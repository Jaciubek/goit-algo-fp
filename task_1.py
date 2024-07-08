class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def insertion_sort(head):
    if not head or not head.next:
        return head
    
    sorted_list = Node(0)  # Dummy node
    current = head
    
    while current:
        prev_sorted = sorted_list
        next_sorted = sorted_list.next
        
        while next_sorted:
            if current.data < next_sorted.data:
                break
            prev_sorted = next_sorted
            next_sorted = next_sorted.next
        
        next_current = current.next
        current.next = next_sorted
        prev_sorted.next = current
        current = next_current
    
    return sorted_list.next

def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return dummy.next

# Example usage of the linked list operations
linked_list = SinglyLinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)
linked_list.append(4)

print("Original List:")
linked_list.print_list()

# Reverse the list
linked_list.head = reverse_list(linked_list.head)
print("Reversed List:")
linked_list.print_list()

# Sort the reversed list using insertion sort
linked_list.head = insertion_sort(linked_list.head)
print("Sorted List using Insertion Sort:")
linked_list.print_list()

# Create two sorted lists and merge them
linked_list1 = SinglyLinkedList()
linked_list1.append(1)
linked_list1.append(3)
linked_list1.append(5)

linked_list2 = SinglyLinkedList()
linked_list2.append(2)
linked_list2.append(4)
linked_list2.append(9)

merged_head = merge_sorted_lists(linked_list1.head, linked_list2.head)
merged_list = SinglyLinkedList()
merged_list.head = merged_head
print("Merged Sorted List:")
merged_list.print_list()