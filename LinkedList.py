"""
---------------------------------------------linkedlist concepts------------------------------------------
"""
class Node:
    # create a node
    def __init__(self, data = None):
        # initialize the first part of node is data
        self.data = data
        # initialize the second part of node is point address of next node
        self.next = None


class Linkedlist:

    # the 1st element of the list is called Head
    # intilizing head = None
    def __init__(self):
        self.head = None

    # function to add elements
    def add(self, item):
        # creating a Node
        node = Node(item)
        node.data = item
        node.next = None
        # if head is None it means the list is empty
        # the first element is to be head
        if self.head is None:
            self.head = node
        # if the list contain elements ,we add the new elements at the end of the list
        else:
            lastNode = self.head
            # traversing to end of the list
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = node

    # creating a function to show the elements
    def printList(self):
        # creating a function to show the elements
        currentNode = self.head
        while currentNode != None:
            # print all the element of the linkedlist
            print(currentNode.data, end=" ")
            currentNode = currentNode.next

    # size of the list
    def len(self):
        # to finding the size of the list by counting each node in the list
        currentNode = self.head
        # take a variable and intilize to 0
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count

    # creating a function to finding the data in given index
    def index(self, index):
        # call function size for length
        length = Linkedlist.len(self)
        if index < 0 or index >= length:
            print("index out of boundary ")
            return
        currentNode = self.head
        count = 0
        # Traversing the list upto to the index and return the data
        while count<index:
            currentNode = currentNode.next
            count += 1
        return currentNode.data

    # creating a function to search a element
    def search(self, word):
        # Initialize current to head
        currentNode = self.head

        # loop till current not equal to None
        while currentNode != None:
            if currentNode.data == word:
                return True  # data found
            currentNode = currentNode.next
        return False

    # Delete a word from that position
    def delete_word(self, word):
        #assinged head to the currentNode
        currentNode = self.head
        # check the list is not empty
        if self.head == None:
            print("List is empty !!Nothing to delete")
        # check the word or key for delete is in start position
        elif currentNode and currentNode.data == word:
            self.head = currentNode.next
            currentNode = None
            return
        # word pop from any position in to the linkedlist
        prevNode = None
        while currentNode and currentNode.data != word:
            prevNode = currentNode
            currentNode = currentNode.next
        if currentNode is None:
            return
        prevNode.next = currentNode.next
        currentNode = None

    # creating function for sort the linkedlist
    def sortlinklist(self, currentNode):
        if self.head == None:
            self.head = currentNode
        else:
            prevNode = self.head
            if prevNode.data > currentNode.data:
                currentNode.next = prevNode
                self.head = currentNode
            else:
                nextNode = prevNode.next
                while prevNode.next != None:
                    if (nextNode.data > currentNode.data):
                        break
                    prevNode = prevNode.next
                    nextNode = nextNode.next
            currentNode.next = nextNode
            prevNode.next = currentNode