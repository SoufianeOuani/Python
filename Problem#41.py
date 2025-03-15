"""
The 41th problem is about to write a program
to calculate the task duration in seconds.
==> Given the time duration of a task int 
the number of days, hours, minutes, and seconds.
"""

Days = int(input("Please enter the number of days : "))
Hours = int(input("Please enter the number of hours : "))
Minutes = int(input("Please enter the number of minutes : "))
Seconds = int(input("Please enter the number of seconds : "))
def TaskDurationInSeconds(Days, Hours, Minutes, Seconds):
    return (Days * 24 * pow(60,2)) + (Hours * pow(60,2)) + (Minutes * 60) + Seconds

print(f"{Days} : {Hours} : {Minutes} : {Seconds} = {TaskDurationInSeconds(Days, Hours, Minutes, Seconds)}")