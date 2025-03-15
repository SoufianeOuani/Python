"""
The 37th is about to ask the user to enter a number
then check if the number prime or not.
"""

Number = int(input("Please enter a number : "))

def CheckPrimeNumber(Number):
    for i in range(2, Number+1):
        if Number % i != 0:
            return True
        else:
            return False
        

if CheckPrimeNumber(Number):
    print(f"{Number} is prime number")
else:
    print(f"{Number} is not prime")