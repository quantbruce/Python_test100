12.判断101-200之间有多少个素数，并输出所有素数。

#### My Method
from math import sqrt

num = 0
list = []

for i in range(101, 200+1):
    for j in range(2, i):  # i 也可以改成int(sqrt(i))+1
        if i % j == 0:   # 就是说，只要有一个能被其他数整除的，这个数就不是质数，后面就不用算了。
            break
    else:
        num += 1
        print(i, '是质数')
print('共有%d个质数' % num)


