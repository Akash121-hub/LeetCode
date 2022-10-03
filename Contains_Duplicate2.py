# 219. Contains Duplicate II
"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         ab_diff = abs(i-j)
        #         if i == j:
        #             continue
        #         if (nums[i] == nums[j] and ab_diff <= k):
        #             return True
        # return False
        for ind,key in enumerate(nums):
            if (key in indices and ind - indices[key] <= k):
                return True
            indices[key] = ind
        return False
        