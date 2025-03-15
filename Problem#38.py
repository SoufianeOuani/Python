"""
The 38th problem is about to write a program to read
TotalBill and CashPaid and calculate the remainder to paid back.
"""

TotalBill = int(input("Please enter the total bill : "))
CashPaid = int(input("Please enter the casha paid : "))

def Remainder(TotalBill, CashPaid):
    return CashPaid - TotalBill


print(f"Total bill = {TotalBill}")
print(f"Cash paid = {CashPaid}")
print(f"Remainder = {Remainder(TotalBill, CashPaid)}")
