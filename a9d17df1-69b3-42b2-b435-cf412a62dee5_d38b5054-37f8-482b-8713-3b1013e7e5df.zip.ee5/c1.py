nums=[]
while 1:
    b=int(input())
    nums.append(b)
    if b==0:break
m=max(nums)
c=nums.count(m)
print(m)
print(c)