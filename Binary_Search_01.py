# Binary search works on sorted lists


from unittest import result


list1 = [2,3,1,4]
list1.sort()
# print(list1)

def search_elem(list5, target):
    list5 = sorted(list5)
    left_idx = 0
    right_idx = len(list5)-1
    # middle_index = 0

    while left_idx <= right_idx:
        middle_index = (left_idx+right_idx) // 2
        middle_number = list5[middle_index]

        if middle_number == target:
            return middle_index
        if middle_number < target:
            left_idx = middle_index + 1
        else:
            right_idx = middle_index - 1
    
    return -1

# print(search_elem([1,2,3,4,5,6,7,8],8))


def binary_search_using_recursive_func(nums_list,target,left_indx,right_indx):
    # left_indx = 0
    # right_indx = len(nums_list) - 1
    middle_index = (left_indx + right_indx) // 2



    if right_indx < left_indx:
        return -1
    if middle_index >= len(nums_list) or middle_index < 0:
        return -1
    middle_number = nums_list[middle_index]
    if middle_number == nums_list[middle_index]:
        return middle_index
    if target < middle_number:
        left_indx = middle_index + 1
    if middle_number > target:
        right_indx = middle_index - 1

    return binary_search_using_recursive_func(nums_list,target,left_indx,right_indx) 


target1 = 18

nums_list1 = [12,23,28,18,90,78,9,0,7]

result1 = binary_search_using_recursive_func(nums_list1,target1,0,len(nums_list1))
print(result1)

