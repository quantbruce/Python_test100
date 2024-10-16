47.题目：两个变量值互换。

#### My Method
def mul_replace(x, y):
    x ,y  = y, x
    print('x=%s, y=%s' % (x, y))


if __name__ == '__main__':
    x = str(input('请输入x：'))
    y = str(input('请输入y：'))
    mul_replace(x, y)
    
    
 #### Answer
 def exchange(a,b):
    a,b = b,a
    return (a,b)
 
if __name__ == '__main__':
    x = 10
    y = 20
    print 'x = %d,y = %d' % (x,y)
    x,y = exchange(x,y)
    print 'x = %d,y = %d' % (x,y)
