elements = [2,3,4,5,2,1,3,10]
first_max = max(elements[0],elements[1])
second_max = min(elements[0], elements[1])
for i in range(2,len(elements)):
    if elements[i] > first_max:
        second_max = first_max
        first_max = elements[i]
    elif elements[i] > second_max and first_max!= elements[i]:
        second_max = elements[i]

print(second_max)