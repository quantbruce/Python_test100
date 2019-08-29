40.题目：将一个数组逆序输出。

####My Method
import numpy as np

def back_output(a):
    b = sorted(a, reverse=True)
    print(b)

if __name__ == '__main__':
    a = np.array((1, 2, 3, 4, 5, 6))
    back_output(a)

## a = np.array((1, 2, 3, 4, 5, 6))  # 这两行是作为参考的另一种写法，需要熟悉
## print(a[::-1])



##### Answer
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a)
    print(a)
    for i in range(len(a) // 2):              # 半渡击之的套路
        a[i],a[N - i - 1] = a[N - i - 1],a[i]   # 首位等距离互换的套路
    print(a)
