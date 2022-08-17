'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. '''

# Example 
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

class Solution:
    def removeDuplicates(self, nums):
        j = 0
        if len(nums) <= 0:
            return
        for i in range(0,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return [j + 1]


S = Solution()
# c = S.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
# print(c)


# Count unique elements

elements = [0,0,1,1,2,2,3,4,4,5,6,6]

def count_unique_elements(nums):
    left = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[left] = nums[i]
            left += 1
    print("nums   -->    ",nums)
    return left
print(count_unique_elements(elements))