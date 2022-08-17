from itertools import count


list1 = [11,22,33,11,11,44,11,22,33]

current_max = 0
for i in list1:
    if list1.count(i) > current_max:
        current_max = i
print(current_max)

from collections import Counter

counter = Counter(list1)
print(counter.most_common(1))

