#随意输入一个三位数，判断是否是水仙花数
#153是一个水仙花数
num = int(input('请输入一个三位数：'))

a = num % 10
b = num // 10 % 10
c = num // 100

if pow(a, 3) + pow(b, 3) +pow(c, 3) == num:
    print('%d是一个水仙花数'%num)
else:
    print('%d不是一个水仙花数'%num)
