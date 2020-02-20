class Node:
    # create a node
    def __init__(self, data = None):
        # initialize the first part of node is data
        self.data = data
        # initialize the second part of node is point address of next node
        self.next = None

class Stack:
    # head is default Null
    def __init__(self):
        self.top = None
        # initialize the variable
        # count the element of stake
        self.count = 0

    # Checks if stack is empty
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    # method to add data to the stack
    # adds to start of the stack
    def push(self, value):
        # stake head is none
        if self.top is None:
            self.top = Node(value)
            self.count += 1
        else:
            #satke head is not none
            pusedNode = Node(value)
            pusedNode.next = self.top
            self.top = pusedNode
            self.count += 1

    # method to remove head from the stack
    def pop(self):
        # check the stack is not empty
        if self.is_empty():
            print("Stack is empty!!")
        else:
            if self.top.next is None:
                self.top = None
                self.count -= 1
            else:
                self.top = self.top.next
                self.count -= 1

    # return the head node data
    def peek(self):
        # check the stake is not empty
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.top.data

    #found the size of the stack
    def size(self):
        #return the count number
        return self.count