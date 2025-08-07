class Stack:
    def __init__(self):
        self.items = [] # Initialize an empty list to hold stack items

    def push(self, item):
        self.items.append(item) # Add an item to the top of the stack

    def size(self):
        return len(self.items) # Return the number of items in the stack

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1] # Return the item at the top of the stack without removing it

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item # Remove and return the item at the top of the stack

