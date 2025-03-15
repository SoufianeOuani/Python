"""
The 17th program is about to calculate the triangle area.
Note : you can use any unit of measurement you want(Cm, m...).
Note : the user should enter a, h.
"""

A = float(input("Please enter A : "))
H = float(input("Please enter H : "))


def Triangle_Area(A,H):
    return (A/2*H)

print(f"Triangle Area = {Triangle_Area(A,H)}")