"""
The 35th problem is about to ask the ask the user
to enter:
Number1, Number2, OperationType.
"""

Number1 = float(input("Please enter the first number : "))
Number2 = float(input("Please enter the second number : "))
OperationType = str(input("Please enter the opertaion type (+, - , * , /) : "))


def SimpleCalculator(Number1, Number2, OperationType):
    if OperationType == '+':
        return Number1 + Number2
    elif OperationType == '-':
        return Number1 - Number2
    elif OperationType == '*':
        return Number1 * Number2
    elif OperationType == '/':
        return Number1 / Number2
    else:
        Number1 + Number2

print(f"{Number1} {OperationType} {Number2} = {SimpleCalculator(Number1, Number2, OperationType)}")
 
