26.题目：利用递归方法求5!。

#### My Method  (虽然求出来了，但是并没有采用递归，递归的要义是函数内部还有调用本身，相当于蛇咬自己尾巴那种感觉)
def factorial_2(n):
    s = 1
    if n < 0:
        print('输入求和项数必须为正数, n>=0 !!!')
    elif n == 0:
        print('0阶乘为: 1')
    else:
        for i in range(1, n+1):
            s *= i
        print('第 %d 项的阶乘为: %.6f' % (n, s))

if __name__ == '__main__':
    n = int(input('请输入要计算阶乘项数n= '))
    factorial_2(n)
    
    
    
    #### Answer
    def factorial_2(n):
    s = 0
    if n < 0:
        print('输入求和项数必须为正数, n>=0 !!!')
    if n == 0:
        s = 1
    else:
        s = n * factorial_2(n-1)
    return(s)     ###################这个细节很重要！！！, 如果此处用print(),就会出现，TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

if __name__ == '__main__':
    n = int(input('请输入要计算阶乘项数n= '))
    factorial_2(5) # 或者可尝试print(factorial_2(5))
