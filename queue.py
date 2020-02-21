class Queue:
    # declaring the front,rare,count variables and initialize
    def __init__(self):
        self.front = None
        self.rare = None
        self.count = 0

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
    # Creating a function for dequeue