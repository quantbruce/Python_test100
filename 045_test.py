45.题目：统计 1 到 100 之和。


#### My Method：

def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    print(s)

if __name__ == '__main__':
    n = int(input('请输入求和的项数n = '))
    sum_n(n)
