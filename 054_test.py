54.题目：取一个整数a从右端开始的4〜7位。

#### My Method
def fun_54(num):
    n = len(str(num))
    if n < 7:
        print('输入数字位数不够！请至少输入一个7位数！')
    else:
        x4 = num % 10**4 // 10**3
        x5 = num % 10**5 // 10**4
        x6 = num % 10**6 // 10**5
        x7 = num % 10**7 // 10**6
        print('倒数第4位数:', x4)
        print('倒数第5位数:', x5)
        print('倒数第6位数:', x6)
        print('倒数第7位数:', x7)

fun_54(7348171926)

#### Answer
if __name__ == '__main__':
    a = int(raw_input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print '%o\t%o' %(a,d)


