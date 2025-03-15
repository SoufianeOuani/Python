"""
The 36th problem is about to read numbers from user and sum them,
keep reading until the user enters -99 then print the sum.
"""


def SumUntil():
    Number = 0
    Sum = 0

    while Number != -99:
        Sum += Number
        Number = int(input("Enter a number : "))

    return Sum

print(f"Sum = {SumUntil()}")