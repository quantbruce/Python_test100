85.题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。


#### My Method

def fun_85(num):
    n = 100
    if num % 2 != 0:
        for i in range(1, n+1): 
            if (10**i-1) % num == 0:    # 我这一步这个关于多少个9的转化写的很出彩！很有创意！
                print(10**i-1)
                print('最少%d 个9除以 %d的结果才为整数' % (i, num))
                break
    else:
        print('输入的是偶数有误！请输入奇数！')


if __name__ == '__main__':
    num = int(input('请输入一个奇数: '))
    fun_85(num)
    
 
 
 ####################################### Other Method
 
 
b=input('input a number:\n')

a=9
n=1
while (1):
    if a%b==0:
        break
    else:
        a=a*10+9
        n=n+1
print '%d 个 9 除于 %d 为整数' % (n,b)
    
    
    
