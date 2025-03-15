"""
The 32th problem is about to ask the user to enter
Grade
then print The grade as follows: 
90 - 100 print A
80 - 89 print B
70 - 79 print C
60 - 69 print D
50 - 59 print E
Otherwise print F
"""

Grade = float(input("Please enter a number : "))


if Grade >= 90 and Grade <= 100:
    print("A")
elif Grade >= 80 and Grade <= 89:
    print("B")
elif Grade >= 70 and Grade <= 79:
    print("C")
elif Grade >= 60 and Grade <= 69:
    print("D")
elif Grade >= 50 and Grade <= 59:
    print("E")
else:
    print("F")