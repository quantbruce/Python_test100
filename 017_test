17.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

text = input('请输入一行字符: ')

def count_fun(text):
    letters = 0
    space = 0
    digit = 0
    others = 0
    i = 0
    while i < len(text):
        s = text[i]
        i += 1
        if s.isalpha():
            letters += 1
        elif s.isspace():
            space += 1
        elif s.isdigit():
            digit += 1
        else:
            others += 1
    print('letter=%d个, space=%d个, digit=%d个, others=%d个' % (letters, space, digit, others))


if __name__ == '__main__':
    count_fun(text)
    
    
    ###Answer
    import string
s = raw_input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
i=0
while i < len(s): # 或在此处用for c in range(s):都可以实现同样效果
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)

