"""
Write a program to ask the user to enter:
Day.
Then print the day according to its number.
"""

Days = int(input("Please enter a day : "))

match Days:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid days.")