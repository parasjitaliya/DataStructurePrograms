class Calendar:

    def calender(self, month, day, year):
        # assigning the year and month values to variable
        y0 = year - (14 - month) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = month + 12 * ((14 - month) // 12) - 2
        d0 = int((day + x + (31 * m0 // 12))) % 7
        # days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
        # return the value
        return d0
    # assign the day for month
    def days(self, month,year):
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        elif month == 2:
            # function calling for leap year
            if Calendar.leap_year(self, year):
                return 29
            else:
                return 28
    # check the year is leap year or not
    def leap_year(self,year):
        return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

    # create the function for print calander
    def print_calander(self, month, day, year):
        # function call for day
        remainder = Calendar.calender(self, month, day, year)
        for date in range(0, remainder):
            print(end="   ")
        # function calll for the day
        lastdate = Calendar.days(self, month, year)
        for date in range(1, lastdate+1):
            # check the condition for day less than 10
            if date < 10:
                print(f" {date}", end=" ")
            else:
                print(date, end=" ")
            # calculate for space
            space = (date + remainder) % 7
            if space is 0 or date is lastdate:
                print("")