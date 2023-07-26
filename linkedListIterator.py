class Node:
    """Represents a linkedlist node"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def get_val(self):
        return self.val


class LinkedListIterator:
    """Iterator for iterating the linked list."""

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current: raise StopIteration
        val = self.current.get_val()
        self.current = self.current.next
        return val


class LinkedList:
    """ListNode represents a node inside a linked list."""

    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)
    
    def add(self, val):
        new_node = Node(val)
        new_node.next, self.head = self.head, new_node


if __name__ == '__main__':
    A = [5, 4, 3, 2, 1]
    head = LinkedList()
    for a in A:
        head.add(a)
    print([a for a in head])
