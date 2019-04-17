i = 1
def hanoi(n, x, y, z):
    global i
    if n == 1:
        print(i, ': ', x, '-->', z)
        i += 1
        # pass
    else:
        hanoi(n-1, x, z, y)
        print(i, ': ', x, '-->', z)
        i += 1
        hanoi(n-1, y, x, z)

hanoi(6, 'x', 'y', 'z')
# print('总共移动了', i, '次')
