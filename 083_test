83.题目：求0—7所能组成的奇数个数。

#### My Method

def fun_83(n):
    sum = 4
    for i in range(1, n+1):
        if i == 1:
            print(sum)
        elif i == 2:
            sum += 4*7
            print(sum)
        elif i > 2:
            sum += 4*7*8**(i-2)
            print(sum)


fun_83(9)
