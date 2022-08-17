from array import array
from operator import indexOf

from arrow import arrow 
# write a program to search for the position of an element in an array using sequential search
'''
nums_arr = array('i',[])

input_arr = int(input("Enter numbers to create array: "))

for i in range(input_arr):
    enter_num = int(input("enter nos:  "))
    nums_arr.append(enter_num)

no_to_find = int(input("Enter no to find:   "))
found = False
for j in range(len(nums_arr)):
    if no_to_find == nums_arr[j]:
        print("the index of given no is :  ", j + 1)
        found = True
    if found == False:
        print("Not found element") '''

try:
    elem =array('i', [1,2,44,5,6])
    pos = elem.index(6)
    print(pos)
except Exception as e:
    print(e)