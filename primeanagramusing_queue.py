"""Add the Prime Numbers that are Anagram in the Range of 0 - 1000
in a Queue using the Linked List and Print the Anagrams from the Queue.
Note no Collection Library can be used.
"""
from queue import Queue, Node
from primeclass import Prime

# creating object of queue class
obj = Queue()

# creating object of prime class
prime_obj = Prime()

# creating prime_anagram list
prime_anagram = []

# creating list of prime number in given range
prime_list = prime_obj.prime(0, 1000)

# checking prime number anagran or not
for num in prime_list:
    if num <= 10:
        continue
    number = prime_obj.anagram(num)
    # check the number is valid or not
    if prime_obj.prime_check(number) and 0 <= number <= 1000:
        prime_anagram.append(num)
# finding the length of prime anagram list
length = len(prime_anagram)

# Adding the prime anagram in to queue
for number in range(length):
    # num=Node(prime_anagram[number])
    obj.enqueue(prime_anagram[number])

# Printind the anagram from queue
obj.print()