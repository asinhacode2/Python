# a simple node class
class Node:
    # constructor
    # a node with a data
    # next pointer set to none
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list to connect many nodes together
class LinkedList:
    # setting a head to node
    def __init__(self):
        self.head = None

    # adding a node
    def append(self, data):
        new_node = Node(data)

        # if the list is empty then head points to this node
        if self.head is None:
            self.head = new_node
            return