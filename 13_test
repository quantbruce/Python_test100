13.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

#### My Method

for x in range(1, 10):
    for y in range(10):
        for z in range(10):
            m = 100*x + 10*y + 1*z
            if x**3 + y**3 + z**3 == m:
                print(m)
                
                
                
               
 ####Answer  
 for n in range(100, 1000):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    if n == i**3 + j**3 + k**3:
        print(n)
time04 = time.time()
 
