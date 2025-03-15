"""
Write a program to read the ATM PIN code from the user,
then check if PIN == 1234, then show the balance to user,
otherwise print "Wrong PIN" and ask the user to re-enter
the PIN again.
Assume user balance is 7500$.
"""

ATMPIN = 1234
PIN = int(input("Enter a valid PIN : "))
FailCount = 2

while FailCount > 0:
    FailCount-=1
    PIN = int(input(f"Wrong PIN, it's still {FailCount + 1} trie(s) : "))

    if ATMPIN != PIN and FailCount == 0:
        print("Wrong PIN")

    if ATMPIN == PIN:
        print("Your balance is 7500$.")
