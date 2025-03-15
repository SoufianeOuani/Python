"""
The 16th program is about to calculate the rectangle area
through diagonal and side area of rectangle.
Note : you can use any unit of measurement you want(Cm, m...).
Note : the user should enter a, d.
"""

from math import sqrt

A = float(input("Please enter A : "))
D = float(input("Please enter D : "))

def RectangleAreaThroughDiagonal(A, D):
    return (A* sqrt((pow(D,2)) - pow(A,2)))


print(f"Rectangle Area Through Diagonal = {RectangleAreaThroughDiagonal(A, D)}")