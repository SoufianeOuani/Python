"""
The 15th program is about to calculate the rectangle area.
Note : you can use any unit of measurement you want(Cm, m...).

Note : The user should enter Length, Width.
"""

Length = float(input("Please enter the length of the rectangle : "))
Width = float(input("Please enter the width of the rectangle : "))

def Rectangle_Area(Length, Width):
    return Length * Width

print(f"Rectangle Area = {Rectangle_Area(Length, Width)} cm")