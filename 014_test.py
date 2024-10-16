14.题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

list_1 = []
num = int(input('请输入一个的数字: '))

def div_prime(num):
    for i in range(2, num):
        while True:
            if num % i == 0:
                list_1.append(i)
                num = num / i
            else:
                break

    print(list_1)

if __name__ == '__main__':
    div_prime(num)
