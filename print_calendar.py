"""
that takes the month and year as command­line arguments and prints the Calendar of the month.
Store the Calendar in an 2D Array,the first dimension the week of the month and the second
dimension stores the day of the week.
"""
# import from the calss
from calendar import Calendar
# object creation for class
obj = Calendar()
# array declaration
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
# check for valid or invalid input
while True:
    try:
        year = int(input("Enter the year  :"))
        month = int(input("Enter the month :"))
        # check for the month is valid or naot
        if month <= 12 and month >= 0 and len(str(year)) == 4:
            break
        else:
            print("Invalid input !!")
    except ValueError:
        print("Invalid input!!")
# print the year and month for head
print(" "f'{month_list[month-1]} {year}')
print(" S  M Tu  W Th  F St")
day = 1
# print the calendar
lastdate = obj.print_calander(month, day, year)


