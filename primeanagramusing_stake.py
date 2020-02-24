"""Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Stack.
using the Linked List and Print the Anagrams in the Reverse Order.
Note no Collection Library can be used."""
# import the class from file
from primeclass import Prime
from stack import Stack, Node

# creating object of stack class
obj = Stack()

# creating object of prime class
prime_obj = Prime()

# creating prime_anagram list
prime_anagram = []

# creating list of prime number in given range
prime_list = prime_obj.prime(0, 1000)

# Checking prime number anagran or not
for num in prime_list:
    if num <= 10:
        continue
    number = prime_obj.anagram(num)
    if prime_obj.prime_check(number) and 0 <= number <= 1000:
        prime_anagram.append(num)
# finding the length of prime anagram list
length = len(prime_anagram)

# Adding the prime anagram in to stack
for number in range(length):

    obj.push(prime_anagram[number])

# Printing in reverse order
for number in range(length):
    data = obj.pop()
    print(data, end=" ")
