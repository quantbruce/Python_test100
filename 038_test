38.


#### My Method
import numpy as np

matrix = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)
print(matrix)

m, n = np.shape(matrix)
print(m, n)

def diag_sum(x):
    sum = 0
    for i in range(m):
        for j in range(n):
            if i == j:
                sum += matrix[i, j]
    print(sum)


diag_sum(matrix)



#### Other Method
# coding: utf-8
"""
    1  2  3
    4  5  6 
    7  8  9
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_ = 0
for i in range(0, 3):
    sum_ += matrix[i][i]
print sum_

