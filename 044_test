44.两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

#### My Method
import numpy as np
import random

m1 = np.array([random.randint(1, 100) for i in range(9)]).reshape(3, 3)
m2 = np.array(range(9, 0, -1)).reshape(3, 3)
print(m2[2, 2] + m2[0, 0])   # 这里不会报错，因为此处是矩阵，可以这样写[x,y]
print(m1)
print(len(m1))
print(m2)
print(m1+m2)



#### Answer
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
        # result[i, j] = X[i, j] + Y[i, j]   # 这样输入会报错，因为上面其实只是列表形式，还没有转化成真正的矩阵形式

for r in result:
    print(r)
