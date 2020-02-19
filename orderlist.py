"""
Read .a List of Numbers from a file and arrange it ascending Order in a
Linked List. Take user input for a number, if found then pop the number out of the
list else insert the number in appropriate position
"""
# Program for UnOrdered List
# Creating Object for Linked List
from LinkedList import Linkedlist
from LinkedList import Node
obj = Node()
listobj = Linkedlist()

# Open and read the file
openfile = open('number.txt', 'r')
# split the word of file
file = openfile.read().split(" ")
openfile.close()
# itretive functoin for add into the linkedlist
for i in file:
    linkNode = Node(int(i))
    listobj.sortlinklist(linkNode)
listobj.printList()
# take user input for search
number = int(input("enter the number for search :"))
# call the function search
result = listobj.search(number)
print(result)
if result:
    listobj.delete_word(number)
    print("After Searching element in the list ")
    #after removing the element
    listobj.printList()
    #Delete the word form the file by over writting.
    file = open('number.txt', 'w')
    file.write('')
    file.close()
    print("\nthe word is deleted.....")
else:
    listobj.add(number)
    print("After searching element in the list ")
    # after adding the element Unordered list
    listobj.printList()
    # adding the word to file
    add_word = Node(number)
    listobj.add(add_word)
    # open the file in append mode
    file = open('number.txt', 'a+')
    file.write(" " + str(number))
    file.close()