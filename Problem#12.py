"""
The 12th problem is about to write a program to ask the user
to enter Number1, Number2
Then print The max Number 
"""

Number1 = int(input("Please enter the first number : "))
Number2 = int(input("Please enter the second number : "))

def GetMaxNumber(Number1, Number2):
    if Number1 > Number2:
        return Number1
    else:
        return Number2
    
print(f"The maximum number is : {GetMaxNumber(Number1,Number2)}")