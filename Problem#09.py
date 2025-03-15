"""
The 9th problem is about wo write a program to ask the user 
to enter Number1, Number2, Number3
Then print the sum of the enetered numbers.
"""

Number1 = int(input("Please enter the first number : "))
Number2 = int(input("Please enter the second number : "))
Number3 = int(input("Please enter the third number : "))

def SumNumbers(Number1, Number2, Number3):
    return (Number1 + Number2 + Number3)

print(f"{Number1} + {Number2} + {Number3} = {SumNumbers(Number1, Number2, Number3)}")