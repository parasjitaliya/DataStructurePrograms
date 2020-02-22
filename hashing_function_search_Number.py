"""
------------Hashing Function to search a Number in a slot---------------
Create a Slot of 10 to store Chain of Numbers that belong to each Slot to
efficiently search a number from a given set of number
"""
# creating Node class
class Node:
    def __init__(self):
        self.data = None
        self.next = None

# creating HashingList class
class HashingList:
    def __init__(self):
        self.node_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def insert(self, data):
        # creating the node and inserting the data and reffer next to None
        n = Node()
        n.data = data
        n.next = None
        # dividing the number with 11 and storing the number in index = remainder
        index = int(data % 11)
        # reading the array element places the in the index
        node = self.node_arr[index]

        # if the node in that index is none adding the data to that node
        if index is node:
            # node = n
            self.node_arr[index] = n

        # else traverse to the end and adding the node to existing node
        # taking temporary variable to store node
        else:
            temp = node
            while temp.next is not None:
                temp = temp.next
            temp.next = n
    # creating a function to display the values
    def display(self):
        # Display the data regarding to the remainder and the index of the node array
        for i in range(len(self.node_arr)):
            print(f'remainder {i} and the values are ', end="")
            # reading the node at the index of the node array
            temp = self.node_arr[i]
            if temp in range(0,11):
                print(None)
            else:
                if temp is not None:
                    # if temp.next is None:
                    #     print("None")
                    while temp is not None:
                        if temp.data is not None:
                            print(temp.data,end=",")
                        temp = temp.next
                    print()

    # print method to store the values into a file
    def Print(self):
        # creating a file to store the values
        file = open("Hashing_function.txt", 'w')
        file.write("")
        file.close()
        # writing the values into the file
        f = open('Hashing_function.txt', "a+")
        for i in range(len(self.node_arr)):
            value = f'remainder {i} and the values are '
            f.write(value)
            # reading the node at the index of the node array
            temp = self.node_arr[i]
            if temp in range(0, 11):
                f.write("None")
            else:
                if temp is not None:
                    while temp is not None:
                        if temp.data is not None:
                            var = f',{temp.data}'
                            f.write(var)
                        temp = temp.next
                    f.write("\n")

# creating an object for HashingList class
obj = HashingList()
count = int(input("enter how many numbers want to insert"))
# reading the values from the user
for i in range(count):
    obj.insert(int(input(f'value{i+1}')))

# Display the list
obj.display()

# to store the values into a file
obj.Print()