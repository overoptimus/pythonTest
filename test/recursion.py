import sys
sys.setrecursionlimit(2000)

def recursion(num):
    if num != 1:
         return num * recursion(num-1)
    else:
        return num


a = recursion(1000)
print(a)
