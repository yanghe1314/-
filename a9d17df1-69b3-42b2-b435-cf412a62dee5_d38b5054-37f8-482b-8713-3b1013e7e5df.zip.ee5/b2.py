import math
x=int(input())
y=int(input())
radius=int(input())
distance = int(math.sqrt((x - 0) ** 2 + (y - 0) ** 2))
if distance < radius:
    print("1")
elif distance == radius:
    print("0")
else : print("-1")