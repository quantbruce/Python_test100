20.题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

## My Methods

def fall_ball(n):
    a0 = 100
    q = 0.5
    an = a0*q**n
    Sn = 1.5*a0*(1-q**n)/(1-q)
    print('第 %d 次反弹高度为%.10f 米' % (n, an))
    print('第 %d 次反弹时, 共经过 %.10f 米' % (n, Sn))

if __name__ == '__main__':
    n = int(input('请输入反弹次数n=：'))
    fall_ball(n)



#### Answer
tour = []
height = []
 
hei = 100.0 # 起始高度
tim = 10 # 次数
 
for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2*hei) 
    hei /= 2
    height.append(hei)
 
print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))
