"""
The 40th problem is about to write a program 
to read a Number Of Hours and calculates
the number of weeks, and days included in that number.
"""

NumberOfHours = int(input("Please enter the number of hours : "))

def DaysInHours(NumberOfHours):
    return NumberOfHours / 24

def WeeksInHours(NumberOfHours):
    return DaysInHours(NumberOfHours) / 7


print(f"{NumberOfHours} ==> {WeeksInHours(NumberOfHours)} weeks.")
print(f"{NumberOfHours} ==> {DaysInHours(NumberOfHours)} days.")