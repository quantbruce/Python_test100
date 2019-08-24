23.打印出星号菱形图像

## Best method
s = '*'
for i in range(1, 8, 2):   # step的取法，自己体会
    print((s*i).center(7))  # 7代表最大宽度，center()也可以换成ljust,rjust.自己体会

for j in reversed(range(1, 6, 2)):  # reversed的用法，自己体会
    print((s*j).center(7))    # 这个循环不是双重循环，而是两个分别的循环。自己体会
    
    
 ## Another ways
 s = '*'

for i in range(1, 8, 2):
    space_num = int((7-i)/2)  # 单侧的
    print(' '*space_num + s*i + ' '*space_num)

for j in reversed(range(1, 6, 2)):
    space_num = (7-j)//2
    print(' ' * space_num + s * j + ' ' * space_num)
