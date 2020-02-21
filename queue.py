class Node:
    # create a node
    def __init__(self, data = None):
        # initialize the first part of node is data
        self.data = data
        # initialize the second part of node is point address of next node
        self.next = None

class Queue:

    # declaring the front,rare,count variables and initialize
    def __init__(self):
        self.front = None
        self.rare = None
        self.count = 0

    # Checks if stack is empty
    def is_empty(self):
        if self.rare is None:
            return True
        else:
            return False

    # creating a function for enqueue
    def enqueue(self, data):
        # creating Node
        node = Node(data)
        node.data = data
        node.next = None
        # if the given element is 1st element, front element = rare element
        if self.rare == None:
            self.front = self.rare = node
        # else given data is assigned next to the rare element
        self.rare.next = node
        self.rare = node
        self.count += 1

    # Creating a function for dqueue
    def dequeue(self):
        if Queue.is_empty(self):
            return "Queue is empty"
        else:
            if self.front.next == None:
                self.front == None
            else:
                self.front = self.front.next
                self.count -= 1
#found the size of the stack
    def size(self):
        #return the count number
        return self.count