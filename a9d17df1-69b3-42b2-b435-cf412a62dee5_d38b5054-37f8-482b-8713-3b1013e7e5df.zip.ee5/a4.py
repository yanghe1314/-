a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:              # 判断是否能构成三角形
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1/2)  # 注意用小括号保证运算优先级
    print(str(a+b+c))
    print('{:.2f}'.format(s))                       # 输出严格保留2位小数，6.00时输出6.00
else:
    print('NO')