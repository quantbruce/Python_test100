101.Python - 获取 100 以内的质数

#### Answer and other
def find_prime_within(n):
    ls = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ls.append(i)
    print(ls)


find_prime_within(100)

#### Other Method
s = [n for n in range(1, 100) if not [m for m in range(2, n) if n % m == 0]]  
print(s)


#### 比较好理解的方式
def find_prime_within(n):
    ls = []
    for i in range(2, n+1):
        flag = True           ## 这个flag要放在for i 循环的下面，程序才是正确的
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag == True:  ### 用flag的套路
            ls.append(i)
    print(ls)

find_prime_within(100)




def find_prime_within_new(n):
    ls = [2]    ## 我按常识就知道2是个质数
    for i in range(2, n+1):
        flag = True
        for j in ls:   ### 这一个降低算法时间复杂度的好技巧，实际上就相当于除数都在质数集合里取，因为如果除数如果是合数的话，能被整除则被除数也必然是合数
            if i % j == 0:
                flag = False
                break
        if flag == True:
            ls.append(i)
    print(ls)

find_prime_within_new(100)
