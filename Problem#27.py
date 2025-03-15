"""
The 21th problem is about print numbers from N to 1.
"""

N = int(input("Please enter the arrive number : "))

# Using for loop.
for i in range(N, 0, -1):
    print(i)

j = 1

#Using while loop.
while N >= j:
    print(N)
    N-=1