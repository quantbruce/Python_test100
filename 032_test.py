32.题目：按相反的顺序输出列表的值。

#### My Method

def rev_output(x):
    t = sorted(x, reverse=True)
    print(t)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rev_output(list)



#### Answer

a = ['one', 'two', 'three']

for i in a[::-1]:
    print(i)




