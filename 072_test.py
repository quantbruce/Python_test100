72.题目：创建一个链表。

#### My Method
def output_list(n):
    list = [input('please input a number: \n') for i in range(1, n+1)]
    print(list)


if __name__ == '__main__':
    n = int(input('请输入需要创建列表的长度n = '))
    output_list(n)
