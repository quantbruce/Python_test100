82.题目：八进制转换为十进制


#### My Method

def oct_to_int(x): # x是待输入的八进制数，n是数的位数
    sum = 0
    n = len(str(x))
    k = []
    for i in range(n):
        if i != n-1:
            k.append(x % 10**(i+1) // 10**i)
        else:
            k.append(x // 10**i)
    # print(k)
    if 8 and 9 not in k:
        for j in range(n):
            sum += k[j]*8**j
        print('该八进制数 %d 转化成10进制数后为: %d' % (x, sum))
    elif 8 or 9 in k:
        print('八进制数取值范围为0~7！请重新输入！')


if __name__ == '__main__':
    n = int(input('请输入一个八进制数: '))
    oct_to_int(n)
    
    
    #### Answer
    
    if __name__ == '__main__':
    n = 0
    p = raw_input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print n
