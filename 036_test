36.

#### My Method

def find_prime(lower, upper):
    list = []
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:   ## 此处是精髓所在！
                    break
            else:
                list.append(num)
    print(list)                   ## 这个print()的缩进位置也很重要。自己体会，否则输出结果相差甚远


if __name__ == '__main__':
    lower = int(input('输入区间最小值: '))
    upper = int(input('输入区间最大值: '))
    find_prime(lower, upper)
