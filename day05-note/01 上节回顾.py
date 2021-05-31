

import datetime

t0 = datetime.date(2012,12,12)
t1 = datetime.date.today()
print(t1)

t2 = datetime.datetime.now()
t3 = datetime.datetime.today()
print(t3)
print(t3 == t2)
print(t1 > t0)

print(t3+datetime.timedelta(days=3))