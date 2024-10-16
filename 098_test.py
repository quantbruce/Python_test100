98.题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。


#### My Method
def fun_98():
    s = input('please input a series of string: ')
    S = s.upper()
    filename = input('please input a filename: ')
    with open(filename, 'w') as f:
        f.write(S)
        print(S)
        f.close()

if __name__ == '__main__':
    fun_98()


#### Answer
if __name__ == '__main__':
    fp = open('test.txt','w')
    string = raw_input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test.txt','r')
    print fp.read()
    fp.close()
    

#### Other Method
import sys

str = input('请输入一个字符串:\n')
with open('test1.txt','w') as f:
    f.write(str.upper())
