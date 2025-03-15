#The 4th problem is about to ask the user to enter his/her "Age", "Driver license"
#Then print "hired" if his/her Age is greater than 21 and s/he has a driver license
#Otherwise print "Rejected".


age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").strip().lower()

if age >= 21 and has_license == "yes":
    print("Hired")
else:
    print("Rejected")