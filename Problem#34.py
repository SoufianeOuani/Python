"""
The 34th problem is about to ask the user to enter:
Pennies, Nickels, Dimes, Quarters, Dollars.

Then calculate the total pennies, total dollars and 
print them on the screen.
"""

Penny_Value = 1
Nickel_Value = 5
Dime_Value = 10
Quarter_Value = 25
Dollar_Value = 100

Penny = int(input("Please enter the number of pennies to change : "))
Nickel = int(input("Please enter the number of nickels to change : "))
Dime = int(input("Please enter the number of dimes to change : "))
Quarter = int(input("Please enter the number of quarters to change : "))
Dollar = int(input("Please enter the number of dollars to change : "))

def Total_Pennies():
    return (Penny * Penny_Value) + (Nickel * Nickel_Value) + (Dime * Dime_Value) + (Quarter * Quarter_Value) + (Dollar * Dollar_Value)


def Total_Nickels():
    return Total_Pennies() / 5


def Total_Dimes():
    return Total_Pennies() / 10


def Total_Quarters():
    return Total_Pennies() / 25


def Total_Dollars():
    return Total_Pennies() / 100

print(f"\nTotal Pennies : {Total_Pennies()}")
print(f"Total Nickels : {Total_Nickels()}")
print(f"Total Dimes : {Total_Dimes()}")
print(f"Total Quarters : {Total_Quarters()}")
print(f"Total Dollars : {Total_Dollars()}")