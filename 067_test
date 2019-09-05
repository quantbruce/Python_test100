67.


#### My Method
def fun_67(n):
    import numpy as np
    lst = []
    for i in range(1, n+1):
        x = int(input('请输入长度为%d数组的第%d个元素= ' % (n, i)))
        lst.append(x)
    ## [lst.append(int(input('请输入长度为%d数组的第%d个元素= ' % (n, i)))) for i in range(1, n+1)]  也可以这样写，比较酷！效率高
    temp_max = max(lst)
    lst[lst.index(max(lst))] = lst[0]
    lst[0] = temp_max

    temp_min = min(lst)
    lst[lst.index(min(lst))] = lst[-1]
    lst[-1] = temp_min

    print(np.array(lst))


if __name__ == '__main__':
    n = int(input('请输入一个数组的长度n= '))
    fun_67(n)
    
    
    ####################################################### Other Method
    
    import numpy as np
a = []
for i in range(5):
    a.append(input("Please input a number: "))
print a
a = np.array(a)
#得到最大值的索引
max_index = np.argmax(a)     #######################得到索引的方法，记住了！是np.argmin()或者np.argmax()
#得到最小值的索引
min_index = np.argmin(a)
a[0], a[max_index] = a[max_index], a[0]
a[-1], a[min_index] = a[min_index], a[-1]
print a


######################Answer
def inp(numbers):
    for i in range(6):
        numbers.append(int(raw_input('输入一个数字:\n')))
p = 0
 
def arr_max(array):
    max = 0
    for i in range(1,len(array) - 1):
        p = i
        if array[p] > array[max] : max = p
    k = max
    array[0],array[k] = array[k],array[0]
def arr_min(array):
    min = 0
    for i in range(1,len(array) - 1):
        p = i
        if array[p] < array[min] : min = p
    l = min
    array[5],array[l] = array[l],array[5]
 
def outp(numbers):
    for i  in range(len(numbers)):
        print numbers[i]
 
if __name__ == '__main__':
    array = []
    inp(array)        # 输入 6 个数字并放入数组
    arr_max(array)    # 获取最大元素并与第一个元素交换
    arr_min(array)    # 获取最小元素并与最后一个元素交换
    print '计算结果：'
    outp(array)

