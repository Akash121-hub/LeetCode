from collections import Counter


list5 = [10,20,30,10,20,20]
res = []
for i in range(len(list5)):
    for j in range(i+1,len(list5)):
        if list5[i] == list5[j] and list5[i] not in res:
            res.append(list5[i])

print(res)


dict1 = Counter(list5)

result = [item for item in dict1 if dict1[item] > 1]
print(result)
