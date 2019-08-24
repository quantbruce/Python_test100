22.题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。


## 解析: 后来看了别人的代码，结合自己的思考，整理出基本思路如下：假设a,b,c的对手分别是i,j,k，将i,j,k所有可能出现的组合先穷举出来，
同时需要满足2个条件：i,j,k不能同时出现（即a,b,c的对手不可能有重复）；
a不对x，c不对x,z，只要满足此2条件就可以。简而言之：用3个for穷举，用2个if限定条件。代码如下：


for i in range(ord('x'), ord('z')+1): #假设a,b,c的对手分别是i,j,k
    for j in range(ord('x'), ord('z')+1): #用3个for穷举i,j,k可能出现的所有组合
        for k in range(ord('x'), ord('z')+1):
            if i != j and i != k and j != k: #条件1：i,j,k不能同时出现
                if i != ord('x') and k != ord('x') and k != ord('z'): #条件2：a不对x，c不对x,z
                    print('a--%s\tb--%s\tc--%s' % (chr(i), chr(j), chr(k)))  # chr()和ord()互为逆运算
