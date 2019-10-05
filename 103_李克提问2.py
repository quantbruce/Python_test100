## 返回一个list前n大的数字的索引

# ls = [3, 2, 5, 6, 7, 3, 4, 7, 7]

ls = [3, 2, 5, 6, 7, 3, 4, 7, 7, 8, 8]
ls2 = sorted(ls, reverse=True)
print(ls)
print(ls2)

output = []
count = 0
n = 4

for i in range(n):
    for j in range(len(ls)):
        if ls2[i] == ls[j] and count < n:
            output.append(j)
            ls[j] = min(ls)  # 不一定要删除掉，可以用最小的替代，免得影响我找后面最大的元素
            count += 1
print(output)
print(ls)
