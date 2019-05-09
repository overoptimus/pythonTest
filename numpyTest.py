import numpy as np

# numpy基本的创建
array = np.array([[1, 2, 3], [4, 32, 6]], dtype=np.int)

print(array.dtype)
print('number of dim', array.ndim)
print('shape:', array.shape)
print('size:', array.size)


print('==============================================================')
array2 = np.zeros((3, 4), dtype=np.float, order='C')
print(array2)

array3 = np.arange(1, 13).reshape((3, 4))
print(array3)

a4 = np.linspace(1, 10, 5)
print(a4)

# numpy的基本运算
print('==============================================================')
a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = a - b
print('c')
print(c)
# python的乘方是**
c = b**2
print('b^2')
print(c)

# 求三角函数
print('==============================================================')
a5 = np.array([30, 60 ,90])
c = np.sin(a5)
print('三角函数：')
print(c)

# 判断数据中的符合某种条件的数据
print(b, b < 3)
print(b == 3)


# 矩阵的乘法
print('==============================================================')
a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape((2,2))
c = a * b
c_dot = np.dot(a, b)
c_dot2 = a.dot(b)

print('矩阵乘法：')
print(c)
print(c_dot)

# ========================================================
print('==============================================================')
# a = np.random.random((3, 4))
a = np.arange(12).reshape(3, 4)
print(a)
print(np.sum(a, axis=1))    # 1 行 0 列
print(np.max(a, axis=0))
print(np.min(a, axis=1))


# ========================================================
print('================================================================================================')
A = np.arange(2, 14).reshape((3, 4))
print(A)
print(np.argmin(A))     # 索引
print(np.argmax(A))
print(np.mean(A))    # 平均数
print(A.mean())     # 平均数
print(np.average(A))    # 平均数
print(np.median(A))     # 中位数
print(np.cumsum(A))     # 累加
print(np.diff(A))       # 相邻之差
print(np.nonzero(A))    # 输出非0元素
print(np.sort(A))       # 逐行排序
print(np.transpose(A)) #矩阵的转置
print(A.T) #矩阵的转置
print(np.clip(A, 4, 7)) #矩阵元素小于4的全变为4，大于9的全变为9


# ==================================================
print('numpy的索引：')
a = np.arange(3, 15).reshape(3, 4)
print(a[1][0])
print(a[1, 0])
print(a[2, :])
print(a[:, 2])
print(a[1, 1:2])
for column in a.T:
    print(column)
print(a.flatten()) # 转变为一维的列表
print(a.flat)

# numpy array的合并
# ==================================================================================
print('numpy array的合并')
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
c = np.array([3, 3, 3])
print(np.vstack((a, b, c)))    # 上下合并 vertical stack
print(np.hstack((a, b)))    # 左右合并 horizontal stack
print(a.shape, b.shape)
print(a[:, np.newaxis]) # 一维的转置
print(np.concatenate((a, b, c), axis=0))
