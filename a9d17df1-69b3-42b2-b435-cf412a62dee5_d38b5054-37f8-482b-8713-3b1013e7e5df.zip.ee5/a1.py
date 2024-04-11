h=int(input())
m=int(input())
s=int(input())
a=m+s
while a>=0:
    if a>=60:
        h+=1
        a=a-60
    else:
        m=a
        a=0
        break
print(h)
print(m)