90.题目：列表使用实例。

matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
# print(matrix)
# print(matrix[1])

col2 = [row[1] for row in matrix]#get a  column from a matrix
print(col2)
col3 = [col[1] for col in matrix]  # 体会和上面的差异，体会异同。不管是填row,col输出结果都一样，说明默认一行一行的看。
print(col3)
col2even = [row[1] for row in matrix if row[1] % 2 == 0]#filter odd item
print(col2even)
