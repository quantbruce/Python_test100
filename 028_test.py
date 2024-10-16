28.题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

#### My Method

def age_count(n):
    for i in range(1, n+1):
        d = 2
        age = 10+(i-1)*d
        print('第 %d 个人 年龄为%d' % (i, age))

if __name__ == '__main__':
    n = int(input('请输入第总人数n = '))
    age_count(n)
    
 
 
 ##### Answer
 def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n-1) + 2    # 用递归的时候，总是要习惯思考下，前一项是后一项的什么，后一项是前一项的什么
    return(c)

if __name__ == '__main__':
    n = int(input('请输入第总人数n = '))
    print(age(n))

 
 
 
