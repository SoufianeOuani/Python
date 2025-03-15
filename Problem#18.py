"""
The 18th program is about to calculate the circle area.
Note : you can use any unit of measurement you want(Cm, m...).
Note : the user should enter r.
"""

import math

R = float(input("Please enter r : "))


def Circle_Area(R):
    return (math.pi * pow(R,2))

print(f"Circle Area = {Circle_Area(R)}")