"""
The 29th problem is about to write a program 
to sum even numbers from 1 to N.
"""

N = int(input("Please enter the arrive number : "))


def SumOddNumbersInRange(N):
    Sum = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            Sum += i
    return Sum


print(f"Sum of odd numbers in the range {N} = {SumOddNumbersInRange(N)}")