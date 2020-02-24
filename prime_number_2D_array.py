# import prime class from primeclass file
from primeclass import Prime

print("Prime number in range  0 to 1000 is :")

# Creating object for prime class
obj = Prime()

# declare a iterator variable to count the loop iterations
# assign the value for variable
itration = 0
# creating an empty list for strong the primes
arr = []
for number in range(0, 1000, 100):
    # calling the prime function to get the prime numbers
    arry = obj.prime(number, number+100)
    # increment the value
    itration += 1
    # append the arry result in to the array
    arr.append(arry)
# calling the function to print all numbers in 2D array
obj.Print(itration)