"""
The 13th problem is about to write a program to 
ask the user to enter 3 numbers: A, B, C
then print the max number
"""

Number1 = int(input("Please enter the first number : "))
Number2 = int(input("Please enter the second number : "))
Number3 = int(input("Please enter the third number : "))

def GetMaxNumber(Number1, Number2, Number3):
    if Number1 > Number2:
        if Number2 > Number3:
            return Number1
    if Number3 > Number2:
        if Number2 > Number1:
            return Number3
    else:
        return Number2
    
print(f"The maximum number is : {GetMaxNumber(Number1,Number2,Number3)}")