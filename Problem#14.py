"""
The 14th problem is about to write a program 
to ask the user to enter Number1, Number2
Then print the two numbers, then swap the two numbers
 and print them
"""

Number1 = int(input("Please enter the first number : "))
Number2 = int(input("Please enter the second number : "))

print(f"Number 1 : {Number1}")
print(f"Number 2 : {Number2}")

temp = Number1
Number1 = Number2
Number2 = temp

print(f"Number 1 : {Number1}")
print(f"Number 2 : {Number2}")