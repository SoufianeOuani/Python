#The 7th problem is about to Write a program to ask the user to enter a number.
#Then print the "Half of the <Number> is <???>".


Number = int(input("Please enter a number : "))

def GetHalfNumber(Number):
    return Number/2

print(f"Half of {Number} is {GetHalfNumber(Number)}")