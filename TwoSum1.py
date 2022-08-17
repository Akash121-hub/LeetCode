# 1. Two Sum
# Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

#  Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# nums = [2,7,11,15], target = 9

def TwoSum(nums, target):
    for i in range(len(nums)):
        # print(i)
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i,j]
                # print(i,j)
            # print(j)

arr1 = [2,7,11,15,5,4]
target1 = 18

# class TwoSumSolution:
# def solution(arr, target):
#     values = {}
#     for i,elem in enumerate(arr):
#         component = target - elem
#         if component in values:
#             return [[values[component], i ], arr[values[component]], arr[i]]
#         values[elem] = i

#     return []
# list1 = solution(arr1,target1)
# print(list1)

ab = " HEllo Word"
str1 = ab.split()



def solution(arr,target):
    values = {}
    for i, elem in enumerate(arr):
        component = target - elem
        if component in values:
            return [values[component], i]
        values[elem] = i

    return []

arr1 = [2,7,11,15,5,4]
target1 = 9
print(solution(arr1,target1))

















        

        