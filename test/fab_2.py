def fab(n):
    oldresult = 0
    result = 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        oldresult = 1
        result = 1
        for i in range(3, n+1):
            temp = result
            result += oldresult
            oldresult = temp
        return result

print(fab(40))
