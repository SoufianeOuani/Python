"""
Write a program that inputs the number of seconds
and change it to days, hours, minutes, seconds
"""

TotalSeconds = int(input("Please enter total seconds : "))

SecondsPerDay = 24 * pow(60,2)
SecondsPerHour = pow(60,2)
SecondsPerMinute = 60


Days = TotalSeconds // SecondsPerDay
Remainder = TotalSeconds % SecondsPerDay

Hours = Remainder // SecondsPerHour
Remainder %= SecondsPerHour

Minutes = Remainder // SecondsPerMinute
Remainder %= SecondsPerMinute

Seconds = Remainder

print(f"{Days}:{Hours}:{Minutes}:{Seconds}")