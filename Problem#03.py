#The 3rd problem is about checking if the entered number is ODD or EVEN.

Number = int(input("Please enter a number : "))

def Odd_Even(Number):
    if(Number % 2 == 0):
        print(f"The number {Number} is EVEN")
    else:
        print(f"The number {Number} is ODD")
        

Odd_Even(Number)