class Node:
    # create a node
    def __init__(self, data = None):
        # initialize the first part of node is data
        self.data = data
        # initialize the second part of node is point address of next node
        self.next = None

class Deque:
    # creating front, rare, count variables
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    # creating a function to inserting elements in front position
    def addfront(self, data):
        #creating a node
        node = Node(data)
        node.data = data
        node.next = None
        # if the inserted element is 1st element then  front_element = rare_element = given 1st element
        if self.front == None:
            self.front = self.rear = node
            self.count += 1
        else:
            # the element will add in front possession
            node.next = self.front
            self.front = node
            self.count += 1

    # creating a function to inserting elements in rare position
    def addRare(self, data):
        #creating a node
        node = Node(data)
        node.data = data
        node.next = None
        # if the given element is first element rare_element = front_element = given element
        if self.rear == None:
            self.rear = self.front = node
            self.count += 1
        else:
            # the given element is added at the end and assigned as rare element
            self.rear.next = node
            self.rear = node
            self.count += 1

    # Function for remove element from front
    def removefront(self):
        # check for the queue is empty or not
        # if the size of the queue is 0 there is no elements to remove
        if self.front == None:
            print("Queue is empty !!nothing to remove")
        # if there is only one one element present
        else:
            if self.front == self.rear:
                node_data = self.front.data
                self.front = self.rear = None
                self.count -= 1
                return node_data
            # else remove the front element and assign next element as front
            else:
                node_data = self.front.data
                self.front = self.front.next
                self.count -= 1
                return node_data

    # Function for removing data from rare
    def removeRear(self):
        # check for the queue is empty or not
        # if the size of the queue is 0 there is no elements to remove
        # print(self.rear.next)
        if self.rear is  None:
            print("Queue is empty !!nothing to remove")
        # if there is only one one element present
        else:
            if self.front == self.rear:
                node_data = self.front.data
                self.front = self.rear = None
                self.count -= 1
                return node_data
                # else remove the rare element and assign next element as rare
            else:
                # traversing upto last but one element and assigned it as rare
                node_data = self.rear.data
                temp = self.front
                while temp.next != self.rear:
                    temp = temp.next
                self.rear = temp
                temp.next = None
                self.count -= 1
                return node_data
    # creating a function to check is empty or not if it is empty return true
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    # Function for getting size of the queue
    def size(self):
        # if the count is < 0 there is an error
        if self.count < 0:
            return print("Error, please restart the program")
        # else return size = count
        else:
            return self.count
