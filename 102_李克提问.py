ls = [1, 2, 3, 0, 1, 9, 8]
ls2 = []
for i in ls:
    ls2.extend(str(sorted(ls).index(i)))

ls2 = [int(x) for x in ls2]

for i in range(len(ls2)):
    for j in range(i+1, len(ls2)):
        if ls2[i] == ls2[j]:
            ls2[j] += 1

print(ls2)






