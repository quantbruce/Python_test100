46.题目：求输入数字的平方，如果平方运算后小于 50 则退出。

#### My Method
def con_square(x):
    s = x**2
    if s < 50:
        print('s<50, 程序结束！')
        return                   ##  此处用quit()也是可以的，但是这两者有何区别呢？
    else:
        print('x的平方为 %d' % s)


if __name__ == '__main__':
    x = int(input('请输入要计算的数字x: '))
    con_square(x)
    

#### Answer

TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print '如果输入的数字小于 50，程序将停止运行。'
again = 1
while again:
    num = int(raw_input('请输入一个数字：'))
    print '运算结果为: %d' % (SQ(num))
    if SQ(num) >= 50:
        again = TRUE
    else:
        again = FALSE
    
