89.题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。


#### My Method

def encode_fun(x):
    ls = []
    for i in x:
        ls.append((int(i)+5) % 10)
    # print(ls)
    if len(ls) == 4:
        ls[0], ls[3] = ls[3], ls[0]
        ls[1], ls[2] = ls[2], ls[1]
        print('The encode four numbers is :',ls)
    else:
        print('要加密的数据只能有四位数！')
        return

if __name__ == '__main__':
    x = list(input('please input four numbers: '))
    encode_fun(x)



#### Other Method

n=raw_input()
n = str(n)
a=[]
for i in range(4):
    a.append(int(n[i])+5)
a[0],a[3]=a[3],a[0]
a[1],a[2]=a[2],a[1]
print "".join('%s' %s for s in a)
