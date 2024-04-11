N = int(input())
SUM = 1
for i in range(2, N + 1):
    if i % 2 == 0:
        SUM += i
    else:
        SUM -= i

print(SUM)