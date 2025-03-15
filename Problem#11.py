"""
The 11th problem is about wo write a program to ask the user 
to enter Mark1, Mark2, Mark3
Then print the average of the enetered numbers.
and print "PASS" if average >= 50, otherwise print "FAIL".
"""

Mark1 = int(input("Please enter the Mark number : "))
Mark2 = int(input("Please enter the Mark number : "))
Mark3 = int(input("Please enter the Mark number : "))

def SumNumbers(Mark1, Mark2, Mark3):
    return (Mark1 + Mark2 + Mark3)

def AverageNumbers(Mark1, Mark2, Mark3):
    return (SumNumbers(Mark1, Mark2, Mark3) / 3)


def Pass_Fail(Mark1, Mark2, Mark3):
    if AverageNumbers(Mark1, Mark2, Mark3) >= 50:
        return "PASS"
    else:
        return "FAIL"
    

print(f"Average = {AverageNumbers(Mark1, Mark2, Mark3)}")
print(Pass_Fail(Mark1, Mark2, Mark3))