elements = [0,4,5,1,3,0,6,9,0]

# Expected Output
# elements = [4,5,1,3,6,9,0,0]
'''size = len(elements)
prev_indx = 0
for i in range(0,size):
    if elements[i] != 0:
        tmp = elements[prev_indx]
        elements[prev_indx]= elements[i]
        elements[i] = tmp
        prev_indx += 1

print(elements)'''

size = len(elements)
previous_indx = 0


for i in range(size):
    if elements[i] != 0:
        temp = elements[previous_indx]
        elements[previous_indx] = elements[i]
        elements[i] = temp
        previous_indx += 1
print(elements)

















