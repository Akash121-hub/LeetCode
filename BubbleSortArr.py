a_string = "0abc 1 def 23 6"
numbers = []
for word in a_string.split():
    for j in word:
        if j.isdigit():
            numbers.append(int(j))
print(numbers)