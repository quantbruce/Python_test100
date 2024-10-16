52.题目：学习使用按位或 | 。

## 体会。不论是与还是或运算，都会转化成2进制来算

if __name__ == '__main__':
    a = 77
    b = a | 3
    print('a | b is %d' % b)
    b |= 7
    print('a | b is %d' % b)
