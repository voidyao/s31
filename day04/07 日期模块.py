

import datetime


# datetime类型： 年月日 时分秒
now = datetime.datetime.now()
print(now,type(now))

today = datetime.datetime.today()
print(today,type(today))

d1 = datetime.datetime.now().strftime("%Y-%m-%d")
print(d1)

# date：年月日
today = datetime.date.today()
print(today)

# time: 时分秒
# datetime.time

now = datetime.datetime.now()
print(now+datetime.timedelta(days=3))
print(now-datetime.timedelta(days=3))
print(now-datetime.timedelta(hours=24*3))







