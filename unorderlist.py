"""
-------------------------------------UnOrdered_List---------------------------------------------
Read the Text from a file,split it into words and arrange it as LinkedList.
Take  a user input to search a Word in the List. if the Word  is not found  then add it to the List,
and if it found  then remove the word  from the list . In the end save the List into a file
"""
# Program for UnOrdered List
# Creating Object for Linked List
from LinkedList import Linkedlist
from LinkedList import Node
obj = Node()
listobj = Linkedlist()

# Open and read the file
openfile = open('abc.txt', 'r')
# split the word of file
file = openfile.read().split(" ")
openfile.close()
# itretive functoin for add into the linkedlist
for i in file:
    listobj.add(i)
# print the linked list
listobj.printList()
# use input
word = str(input("\nenter the word for check:"))
# call the function search
result = listobj.search(word)
print(result)

if result:
    listobj.delete_word(word)
    print("After Searching element in the list ")
    #after removing the element
    listobj.printList()
    #Delete the word form the file by over writting.
    file = open('abc.txt', 'w')
    file.write('')
    length = listobj.size()
    f = open('abc.txt', 'a+')
    # write word of linked list into the file
    for i in range(0, length):
        file.write(" "+listobj.index(i))
    file.close()
    print("\nthe word is deleted.....")

else:
    listobj.add(word)
    print("After searching element in the list ")
    # after adding the element Unordered list
    listobj.printList()
    # adding the word to file
    add_word = Node(word)
    listobj.add(add_word)
    # open the file in append mode
    file = open('file1', 'a+')
    file.write(" " + word)
    file.close()



