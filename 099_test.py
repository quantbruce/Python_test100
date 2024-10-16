099.题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

#### Answer

if __name__ == '__main__':
    import string
    fp = open('test_a.txt')
    a = fp.read()
    fp.close()

    fp = open('test_b.txt')  
    b = fp.read()
    fp.close()

    fp = open('test_c.txt', 'w')
    l = list(a + b)
    l.sort()
    s = ''              ## 这两行得手法很重要，这个是将输出从一般列表形式，转化为普通字符串得输出！
    s.join(l)
    fp.write(l)
    fp.close()
    
    
