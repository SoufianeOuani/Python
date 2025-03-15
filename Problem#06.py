#The 6th problem is to ask the user to enter "FirstName" and "LastName".
#The print full name on the screen.
"""
Example input:
Soufiane
Ouani

Output ==> Soufiane OUani
"""

FirstName = str(input("Please enter your first name : "))
LastName = str(input("Please enter your last name : "))

def GetFullName(FirstName, LastName):
    return f"Full Name : {FirstName} {LastName}"

print(GetFullName(FirstName, LastName))