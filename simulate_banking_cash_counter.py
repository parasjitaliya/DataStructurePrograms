"""Create a Program which creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. Have an input panel to add people
to Queue to either deposit or withdraw money and dequeue the people. Maintain
the Cash Balance.
"""
from queue import Queue

# creating object for Queue Class
obj = Queue()
exit_b = 0
count = int(input("enter the number of persons initially"))
# en-queue the persons one by one using loop
for i in range(count):
    obj.enqueue(1)
while count > 0:
    if count == 0:
        break
    # value assign to the variable
    total_money = 50000
    # printing the options available for customer
    print("--------------Welcome--------------")
    print(" 1  Deposit")
    print(" 2  WithDraw")
    print(" 3  Add persons to queue")
    print(" 4  exit from queue")
    print(" 5  to see the balance money at the cashier ")
    print(" 6  remaining members in the queue")
    inp = int(input("enter  the choice"))
    if inp > 6 or inp <= 0:
        # if the customer entered wrong choice print an error message
        print("Entered wrong selection, Please choose correct one")
        break
    elif inp == 1:
        # 1 for Deposit the money
        deposit = int(input("enter the amount to be deposit"))
        # add the deposited money to total money
        total_money = total_money + deposit
        print(f'{deposit} amount is deposited')
        print(f'{total_money} is your total amount in your account ')
        #check valid input or not and handle the exception
        while True:
            try:
                exit_b = int(input("you want to exit then press 1 else 2"))
                if exit_b is 1:
                    # call the method for exit
                    obj.dqueue()
                    # calculate the count after exit
                    count = count-1
                    break
                elif exit_b is 2:
                    break
            except:
                print("Entered wrong selection, Please choose correct one")

    elif inp == 2:
        # 2 for WithDraw
        withdraw = int(input("enter the withdraw amount"))
        # deducting the withdraw money from total money
        total_money = total_money - withdraw
        print(f'{withdraw} amount is deposited ')
        print(f'{total_money} is your total amount in your account ')
        # check valid input or not and handle the exception
        while True:
            try:
                exit_b = int(input("you want to exit then press 1 else 2"))
                if exit_b is 1:
                    # call the method for exit
                    obj.dqueue()
                    # calculate the count after exit
                    count = count - 1
                    break
                elif exit_b is 2:
                    break
            except:
                print("Entered wrong selection, Please choose correct one")

    elif inp == 3:
        # 3 adding persons into queue
        persons = int(input("enter the how many member are to be add into the queue"))
        # increasing the count by persons
        count = count+persons
        # enqueue that persons
        # using the loop to enqueue 1 person at a time
        for i in range(persons):
            obj.enqueue(1)
    elif inp == 4:
        # 4 exit a person from the queue
        obj.dequeue()
        count = count-1
    elif inp == 5:
        # 5 to show the balance money at the cashier
        print(f'Balance is {total_money} ')
        # check valid input or not and handle the exception
        while True:
            try:
                exit_b = int(input("you want to exit then press 1 else 2"))
                if exit_b is 1:
                    # call the method for exit
                    obj.dqueue()
                    # calculate the count after exit
                    count = count - 1
                    break
                elif exit_b is 2:
                    break
            except:
                print("Entered wrong selection, Please choose correct one")

    elif inp == 6:
        #6 total persons in the queue
        print("reaming persons in the queue", obj.size())

    count = obj.size()
