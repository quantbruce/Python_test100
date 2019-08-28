29.题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。


#### Answer
def fun_29(s):
    a = s // 10000
    b = s % 10000 // 1000
    c = s % 1000 // 100
    d = s % 100 // 10
    e = s % 10
    if len(str(s))>5:
        print('输入的位数大于5有误！ 请重新输入')
        return
    if s < 0:
        print('请输入一个正整数！')
        return
    elif a != 0:
        print('5位数', e, d, c, b, a)
    elif b != 0:
        print('4位数', e, d, c, b)
    elif c != 0:
        print('3位数', e, d, c)
    elif d != 0:
        print('2位数', e, d)
    elif e != 0:
        print('1位数', e)

if __name__ == '__main__':
    n = int(input('请输入数字n ='))
    fun_29(n)
    
 ################################# Maybe Best Method
    def backn(n):
    ls = str(n); s = len(ls)
    ls = ls[s-1:0:-1] + ls[0]
    return ls, s

print(backn(12346))
    
 ###############################  Best Method
num = list(input('输入一个最多5位的数字:'))   # 这一步很关键，可以在一开始输入的时候，就将一个元素用列表打散成若干个数字
print(len(num))
num.reverse()
for i in range(len(num)):
    print(num[i], end='')           # 这个end=''的细节也很重要，因为可以使默认的end='\n'竖着排列变成 横行排列，紧贴着的
    
    
    
