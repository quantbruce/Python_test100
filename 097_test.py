97.题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。


#### Answer
filename = input('please input a filename:')
fp = open(filename, 'w')
ch = ''

# while ch!= '#':
while '#' not in ch:
    fp.write(ch)
    print('', end='\n')
    ch = input('please input characters: ')
fp.close()
