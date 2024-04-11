a=int(input())
n=int(input())
sum=0
tmp=a
for i in range(1,n+1):
    sum=sum+a
    a=a*10+tmp
print(sum)
