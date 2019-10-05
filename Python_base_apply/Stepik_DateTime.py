import datetime
a = input()
b = input()
f = datetime.date(int(a.split()[0]), int(a.split()[1]), int(a.split()[2]))
d = datetime.timedelta(int(b))
print((f + d).year, (f + d).month, (f + d).day)
