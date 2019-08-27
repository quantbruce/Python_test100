25.题目：求1+2!+3!+...+20!的和。

#### My Method

def factorial(n):
    item = 1
    sum = 0
    if n == 0:
        print('前0项的阶乘和为: 1')
    elif n < 0:
        print('输入求和项数必须为正数, n>=0 !!!')
    else:
        for i in range(1, n+1):
            item *= i
            sum += item
        print('前 %d 项的阶乘和为: %.6f' % (n, sum))


if __name__ == '__main__':
    n = int(input('请输入要计算阶乘累加和项数n= '))
    factorial(n)


#### Answer
# -*- coding: UTF-8 -*-
 
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print '1! + 2! + 3! + ... + 20! = %d' % s
