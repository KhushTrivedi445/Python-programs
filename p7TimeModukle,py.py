"""
EXERCISE:
Create a python program capable of greeting you with Good Morning,Good Afternoon and Good Evening.
Your program should use time module to get the current hour.
"""

import time
timestamp=time.strftime('%H')
print("Hour is:",timestamp)
timestamp=time.strftime('%M')
print("Minutes is: ",timestamp)
timestamp=time.strftime('%S')
print("Seconds is:",timestamp)
timestamp=time.strftime('%H:%M:%S')
print("The time is:",timestamp,end="\n\n")

print("Now we have to wish according to time\n\n")
h=int(time.strftime('%H'))
if(h<12 and h>=4):
    print("Good morning sir")
elif(h>=12 and h<16):
    print("Good afternoon sir")
elif(h>=16 and h<20):
    print("Good evening sir")
else:
    print("Good night")

