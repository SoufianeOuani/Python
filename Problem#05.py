#The 5th problem is about to ask the user to enter his/her Age and driver license
#if Age >= 21 and Has a driver license ==> Hired
#otherwise Rejected
#if Has Recommendation Hired.


age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").strip().lower()
has_recommendation = input("Do you have a recommendation (yes/no): ").strip().lower()

if age >= 21 and has_license == "yes" or has_recommendation == "yes":
    print("Hired")
else:
    print("Rejected")