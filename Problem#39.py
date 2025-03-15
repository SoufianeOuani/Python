"""
The 39th problem is about to write a program to read BillValue
and add service fee and sales tax to it, 
and print the TotalBill.

Note : service fee = 10% and sales tax = 16%
"""

BillValue = int(input("Please enter the bill value : "))

def TotalBill(BillValue):
    return BillValue * 1.1 * 1.16


print(f"Total bill = {TotalBill(BillValue)}")