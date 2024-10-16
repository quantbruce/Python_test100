61.


#### Answer  + other

from sys import stdout

def yanghui(i, j):
    if i == j or j == 1:
        return 1
    else:
        return yanghui(i-1, j-1) + yanghui(i-1, j)


for i in range(1, 20):
    for j in range(1, i+1):
        stdout.write(str(yanghui(i, j)))
        stdout.write(' ')
    print()
