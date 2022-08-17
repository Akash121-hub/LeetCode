str_dup = str(set("abcdeabcde"))
# print(str_dup)
without_dup = " "
for i in str_dup:
    if i not in without_dup:
        without_dup = without_dup + i
print(without_dup) 