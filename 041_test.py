41.题目：模仿静态变量的用法。

def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1

if __name__ == '__main__':
    for i in range(3):
        varfunc()


class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)


print(Static.StaticVar)
a = Static()         # 这里Static()要用中间变量a表示, 否则下面循环体中的a.varfunc会报错
for i in range(3):
    a.varfunc()
