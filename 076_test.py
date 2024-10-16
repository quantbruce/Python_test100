76.题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

####  My Method

def fun_76(n):
    sum = 0
    if n % 2 == 0:
        for i in range(1, n+1, 1):
            sum += 1/i
        print(sum)
    else:
        for i in range(1, n+1, 2):
            sum += 1/i
        print(sum)

import time

if __name__ == '__main__':
    # n = int(input('请输入要计算的数列项数n = '))
    n = 0
    m = 1000
    time1 = time.time()
    for i in range(m):
        n += 1
        fun_76(n)
    time2 = time.time()
    print('计算 %d 项总耗时%.6f' % (m, time2-time1))


############# Answer

def peven(n):
    i = 0
    s = 0.0
    for i in range(2,n + 1,2):
        s += 1.0 / i   # Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
    return s
 
def podd(n):
    s = 0.0
    for i in range(1, n + 1,2):
        s += 1.0 / i    # Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
    return s
 
def dcall(fp,n):
    s = fp(n)
    return s
 
if __name__ == '__main__':
    n = int(raw_input('input a number:\n'))
    if n % 2 == 0:
        sum = dcall(peven,n)
    else:
        sum = dcall(podd,n)
    print sum
