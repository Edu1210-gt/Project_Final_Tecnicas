

class Cola:
    """
    A simple Queue (FIFO) implementation using a Python list.

    This class provides basic queue operations such as enqueue, dequeue,
    peek, and checking whether the queue is empty. Items are added at the
    end of the list and removed from the front, following a First-In
    First-Out behavior.

    Methods:
        enqueue(item): Adds an item to the end of the queue.
        dequeue(): Removes and returns the item at the front of the queue.
                   Returns None if the queue is empty.
        peek(): Returns the item at the front of the queue without removing it.
                Returns None if the queue is empty.
        is_empty(): Returns True if the queue has no items, False otherwise.
        __len__(): Returns the number of items in the queue.
        to_list(): Returns a shallow copy of the queue as a list.
    """
     
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        return None if self.is_empty() else self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def to_list(self):
        return list(self.items)
