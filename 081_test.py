81.809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。

#### My Method

for i in range(10, 100):
    condition1 = 809*i == 800*i + 9*i
    condition2 = 999 < 809 * i < 10000
    condition3 = 9 < 8 * i < 100
    condition4 = 99 < 9 * i < 1000
    while condition1 and condition2 and condition3 and condition4:
        print('满足该条件的两位数为%d, 且809*%d=%d' % (i, i, 809*i))
        break


#### Answer
a = 809
for i in range(10,100):
    b = i * a
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print b,' = 800 * ', i, ' + 9 * ', i
