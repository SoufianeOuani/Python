"""
The 33th problem is about to write a program
to ask the user to enter TotalSales.
"""

TotalSales = float(input("Please enter the Total Sales : "))


def Commission(TotalSales):
    if TotalSales >= 1000000:
        return TotalSales * 0.01
    elif TotalSales >= 500000:
        return TotalSales * 0.02
    elif TotalSales >= 100000:
        return TotalSales * 0.03
    elif TotalSales >= 50000:
        return TotalSales * 0.05
    else:
        return TotalSales * 0.00
    

print(f"The Total Commission = {Commission(TotalSales)}")