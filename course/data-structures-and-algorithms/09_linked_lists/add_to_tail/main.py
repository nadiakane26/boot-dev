from node import Node

# https://www.geeksforgeeks.org/dsa/insert-node-at-the-end-of-a-linked-list/

class LinkedList:
    def add_to_head(self, node):
        node.set_next(self.head)
        self.head = node
        if self.tail is None: # set the tail reference to the given node if the list is empty.
            self.tail = node

    def add_to_tail(self, val):
        new_node = Node(val)
        # If there isn't a head node, set the new node as the head and be done.
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        self.tail.set_next(new_node) # Instead of iterating to find the last node, use the tail reference to append the new node
        self.tail = new_node
        # #  keep a reference to the "last" node in the list
        # last = None
        # for current_node in self:
        #     last_node = current_node
        # last_node.set_next(new_node)
        

    # don't touch below this line

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
