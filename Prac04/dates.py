#1
import datetime

today = datetime.date.today()
five_days_ago = today - datetime.timedelta(days=5)

print(five_days_ago)

#2
import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)

#3
import datetime

dt = datetime.datetime.now()
dt_no_microseconds = dt.replace(microsecond=0)

print(dt_no_microseconds)

#4
import datetime

d1 = datetime.datetime(2026, 2, 20, 12, 0, 0)
d2 = datetime.datetime(2026, 2, 23, 15, 30, 0)

diff_seconds = int((d2 - d1).total_seconds())
print(diff_seconds)
