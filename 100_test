100.题目：列表转换为字典。


#### Answer
list = ['Jordan', 'Bruce', 'Kobe', 'James', 'Masato']
height = [198, 173, 198, 203, 174, 180]
print(dict(zip(list, height)))


#### Other Method
r = range(ord('a'), ord('z') + 1)
a = (i for i in r)
b = map(chr, r)
print(dict(zip(a, b)))


#### zip()、map()函数得用法，顺便学习
###体会：zip()相对于，让两个列表里得元素以元组的形式，两两配对，数目以列表元素较少得为准，多出的不会显示。
###体会：map()相对于，R里面得pply家族，实现批量化向量化运算，输进去一个计算列表，通过该函数分别计算，映射输出一个对应计算列表


### zip()函数
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
d = ['k','b','1','8']

zipped = zip(a, b)
print(zipped)
print(list(zipped))
print(list(zip(a, b, c, d)))  # 可以zip多个，记住了！而且是混合的
print(dict(zip(a, d)))
a1, a2 = zip(*zip(a, b))  # 相当于把拉链拉开，就是逆运算
print(a1)
print(list(a1))
print(a2) # 这样默认得输出格式是tuple
print(list(a2)) # 这样输出得格式就是dict


#### map()函数
list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [3, 4, 5, 6, 7]
list_3 = [10, 20, 30]

map_result = map(lambda x, y, z: x**2+y*2+z, list_1,list_2, list_3)
print(list(map_result))
