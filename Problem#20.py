"""
the 20th problem is about check if the number 
is between 18 and 45 ==> print "Valid Age"
otherwise ==> print "Invalid Age" and re-ask the user to enter a valid age.
Note : You should keep asking the user to enter a valid age until s/he enters it.
"""

Age = int(input("Please enter your age : "))

while Age < 18 or Age > 45:
    print(f"{Age} is an invalide age.")
    Age = int(input("Please enter your age : "))

print(f"{Age} is a valide age.")