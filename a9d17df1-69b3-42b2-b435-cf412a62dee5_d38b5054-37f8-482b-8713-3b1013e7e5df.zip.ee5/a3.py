a = input()

if len(a) == 4 and a.isdigit():
	# 逆序切片的结果与a做比较
    if a[::-1] == a:
        print("True")
    else:
        print("False")
else:
    print('输入有误')
