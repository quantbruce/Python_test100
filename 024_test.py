24.题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

#### My Method
def sum_fib_frac(n): # n是项数
    # 分子部分
    list_1 = []
    list_1.extend([2, 3])
    for i in range(1, n-1):
        list_1.append(list_1[-1]+list_1[-2])
    print(list_1)

    # 分母部分
    list_2 = []
    list_2.extend([1, 2])
    for j in range(1, n-1):
        list_2.append(list_2[-1]+list_2[-2])
    print(list_2)

    # 整合分子分母对应项使之称为分式
    list_3 = []
    for k in range(n):
        list_3.append(list_1[k]/list_2[k])
    print(list_3)
    print('该数列前 %d 项的求和为 %.6f' % (n, sum(list_3)))


if __name__ == '__main__':
    n = int(input('请输入要求和的项数n: '))
    sum_fib_frac(n)



#### Answer (Best Method)
def sum_like_fib(n):
    a = 2
    b = 1
    s = 0
    for i in range(1, n+1):  # 观察，在此处循环了n次，其实就计算到这个数列的第n项
        s += a/b   # 观察前后面一项的分子，其实就是前面一项的分子分母的和
        t = a     # 提前找个中间变量，丢包
        a = a + b # 观察，后面一项的分母，其实就是前面一项的分母，
        b = t
    print('该数列前 %d 项和为 %.6f: ' % (n, s))


if __name__ == '__main__':
    n = int(input('请输入需要计算的项数n= '))
    sum_like_fib(n)
    
    
 #### Another Method 小细节！！系列解包赋值，还来不及改变。
 def sum_like_fib2(n):
    a = 2
    b = 1
    s = 0
    for i in range(1, n+1):
        s += a/b
        b,a = a, a+b  # 这个序列解包赋值，从右边一起往左边看，此时b还是未发生变化之前的b!!!细节
    print('该数列前 %d 项和为 %.6f' % (n, s))

if __name__ == '__main__':
    n = int(input('请输入需要计算的项数n= '))
    sum_like_fib2(n)



