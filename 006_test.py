### My Method

ls = []
list = []

def Fib_Seq(n):
    if n == 1:
        ls.append(1)
        print(ls)
    elif n == 2:
        ls.extend([1, 1])
        print(ls)
    elif n > 2:
        ls.extend([1, 1])
        for i in range(2, n):
            ls.append(ls[-1] + ls[-2])
        print(ls)

Fib_Seq(9)



## Answer
## 如果只要输出最后一个。自己找规律
def fib(n):
    a, b = 1, 1
    for i in range(n-1): # 自己多写几行，规律便可以出来了。
        a, b = b, a+b
    print(a)

fib(9)

# 规律摸索(套路总结)
i=1  a=1  b=2
i=2  a=2  b=3
i=3  a=3  b=5
i=4  a=5  b=8
i=5  a=8  b=13
i=6  a=13 b=21
i=7  a=21 b=34
i=8  a=34 b=55   range(n-1)对应print(a)  range(n-2)对应print(b)
......



