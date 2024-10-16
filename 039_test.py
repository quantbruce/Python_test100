39.

#### My Method
def very_insert(x, n):
    # 列表排序
    L = []
    for i in range(n):
        L.append(int(input('列表共有%d个元素，请依次输入列表L中的%d个数字: ' % (n, i+1))))
    S = sorted(L)
    print('该排序后的列表为:', S)
    # 插入部分
    # 插入最左边
    if x <= S[0]:
        S.insert(0, x)
        print('元素 %d 插入的位置是第 %d 位' % (x, S.index(x)))
        print('插入排序后的列表为: ', S)
    # 插入最右边
    elif x >= S[-1]:
        S.insert(len(S)+1, x)
        print('元素 %d 插入的位置是第 %d 位' % (x, S.index(x)))
        print('插入排序后的列表为: ', S)
    # 插入中间部分
    else:
        for i in range(len(S)):
            if S[i] < x < S[i+1]:
                S.insert(i+1, x)
        print('元素 %d 插入的位置是第 %d 位' % (x, S.index(x)))
        print('插入排序后的列表为: ', S)


if __name__ == '__main__':
    x =  int(input('请输入要插入的元素 x ='))
    n = int(input('请输入初始列表的长度n = '))
    very_insert(x, n)
    
    
    
    #### Answer
    if __name__ == '__main__':
    # 方法一 ： 0 作为加入数字的占位符   # 这个思路是个亮点，还是要学习下
    a = [1,4,6,9,13,16,19,28,40,100,0]
    print '原始列表:'
    for i in range(len(a)):
        print a[i],
    number = int(raw_input("\n插入一个数字:\n"))
    end = a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    print '排序后列表:'
    for i in range(11):
        print a[i],
    
    
