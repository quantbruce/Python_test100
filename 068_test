68.题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数


#### My Method
def fun_68(n, m):
    list_1 = []
    [list_1.append(int(input('请输入长度为%d数组的第%d个元素= ' % (n, i)))) for i in range(1, n + 1)]
    list = []
    list.extend(list_1[-m:])
    list.extend(list_1[:-m])
    print(list)


if __name__ == '__main__':
    fun_68(10, 3)
