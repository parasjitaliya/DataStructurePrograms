# create prime class
class Prime:
    # create constructor
    def __init__(self):
        self.list = []

    # creating a function for prime numbers
    def prime(self, range1, range2):
        # an empty list to store the prime number the start to end
        primearr = []
        for num in range(range1, range2 + 1):
            if Prime.prime_check(self, num):
                # append the number in to the array list
                primearr.append(num)
        self.list.append(primearr)
        return primearr

    # function for printing the 2d array
    def Print(self, itr):
        for num in range(itr):
            print(self.list[num])

    # To check number is prime or not
    def prime_check(self, num):
        if num < 2:
            return False
        # declare and initialize the variable for count
        count = 0
        for number in range(2, (num // 2) + 1):
            if num % number == 0:
                count += 1
                return False
        if count == 0:
            return True

    # crating a function to get the anagram number
    def anagram(self, num):
        temp = 0
        while num >= 10:
            temp = (temp * 10) + (num % 10)
            num = num // 10
        temp = (temp * 10) + (num % 10)
        return temp
