#calender
'''import calendar
year=2026
month=6
print(calendar.month(year,month))'''

'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
year=int(input())
print(calendar.calendar(year))'''

'''import calendar
year=int(input())
month=int(input())
print(calendar.month(year,month))'''

#date and time
'''
from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

import time
a=time.time()
print(a)#epoch time
b=time.localtime(a)
print(b)
print(f"Today date is:{b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"Time is : {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"This day is : {b.tm_wday},{b.tm_yday}")

