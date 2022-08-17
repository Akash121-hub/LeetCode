# Reverse list at place

from turtle import right


rev_list = [1,2,3,4,5,6]

left_index = 0
right_index = len(rev_list) - 1

while left_index <= right_index:
    temp = rev_list[left_index]
    rev_list[left_index] = rev_list[right_index]
    rev_list[right_index] = temp
    left_index += 1
    right_index -= 1

print(rev_list)