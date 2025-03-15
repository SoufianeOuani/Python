"""
the 19th problem is about check if the number 
is between 18 and 45 ==> print "Valid Age"
otherwise ==> print "Invalid Age".
"""

Age = int(input("Please enter your age : "))

def ValidateAge(Age):
    if Age >= 18 and Age <= 45:
        print(f"{Age} is a valide age.")
    else:
        print(f"{Age} is an invalide age.")


ValidateAge(Age)