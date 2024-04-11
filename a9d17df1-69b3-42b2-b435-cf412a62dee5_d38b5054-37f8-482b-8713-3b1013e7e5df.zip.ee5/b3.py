import calendar
n=int(input())
y=int(input())
r=int(input())
last_day = calendar.monthrange(n, y)[1]
print(str(last_day-r))