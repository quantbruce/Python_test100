27.题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def reoutput(s, l):
    list = []
    if l == 0:
        return
    else:
        print(s[l-1])
        reoutput(s, l - 1)


if __name__ == '__main__':
    s = input('Please input a String:')
    l = len(s)
    reoutput(s, l)
