19.题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

def wanshu(num):
    for i in range(2, num+1):
        k = []  # 用来收集所有因子
        n = -1   # 用来计算因子的数目(这里起点设置故意比0少一个，是为了让最后输出‘+’数目正好)
        s = i   # 把取出的数赋值给另一个变量s,用于与所有因子作差，若果减去所有的因子后结果为0，这个数即为完数。
        for j in range(1, i):  # 查找因子
            if i % j == 0:  # 找出因子
                n += 1      # 计数
                s -= j      # 与因子作差
                k.append(j)  # 收集所有因子
            else:
                continue

        if s == 0:
            print('打印完数: ', i, end='\n')
            for q in range(n):
                print(str(k[q]), end='+')  # 把之间含‘+’的全部输入，‘+’的数目就是n-1
            print(k[n])  # 把k中最后一个数也补上，但是它后面不再需要'+'


if __name__ == '__main__':
    num = int(input('请输入一个整数: '))
    wanshu(num)
