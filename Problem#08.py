"""
The 8th program is about to write a program to ask the user"
to enter a Mark, Then print "Pass" if MArk >= 50, otherwise"
"Fail""
"""

Mark = int(input("Please enter a mark : "))

def CheckPassFail(Mark):
    if Mark >= 50:
        return "Pass"
    else:
        return "Fail"
    
print(CheckPassFail(Mark))