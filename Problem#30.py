"""
The 30th problem is about to calculate factorial of N!
Example : 6! ==> 6*5*4*3*2*1 = 720
Note : User should enter only positive numbers, otherwise rejects
and ask to enter again. 
"""


Number = int(input("Please enter a number : "))


def Factorial(Number):
    Factorial = 1
    for i in range(1, Number+1):
        Factorial *= i

    return Factorial


print(f"{Number}! = {Factorial(Number)}")