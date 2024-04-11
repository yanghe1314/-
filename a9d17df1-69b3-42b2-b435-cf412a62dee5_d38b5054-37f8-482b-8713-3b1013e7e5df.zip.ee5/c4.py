year=int(input())
month=int(input())
day=int(input())
list=[31,60,91,121,152,182,213,244,274,305,335,366]

if month==1:
    count=day
if (year%4==0 and year%100!=0)or year%400==0:
    if month>1 and month<13:
        count=list[month-2]+day
else:
    if month>1 and month<13:
        count=list[month-2]+day-1
print(str(count))
