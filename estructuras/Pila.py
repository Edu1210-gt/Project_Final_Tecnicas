

class Pila:
    """
    A simple Stack (LIFO) implementation using a Python list.

    This class provides all basic stack operations such as pushing an item,
    popping the top item, checking the top element without removing it, and
    verifying whether the stack is empty. It follows a Last-In First-Out (LIFO)
    behavior where the most recently added item is the first to be removed.

    Methods:
        push(item): Adds an item to the top of the stack.
        pop(): Removes and returns the item at the top of the stack.
               Returns None if the stack is empty.
        peek(): Returns the item at the top of the stack without removing it.
                Returns None if the stack is empty.
        is_empty(): Returns True if the stack has no items, False otherwise.
        __len__(): Returns the number of items in the stack.
        to_list(): Returns a shallow copy of the stack as a list.
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        return None if self.is_empty() else self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def to_list(self):
        return list(self.items)
