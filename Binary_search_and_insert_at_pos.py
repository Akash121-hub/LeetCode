class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1

        if target not in nums:
            nums.append(target)
            nums.sort()
            res = nums.index(target)
            return res
                
        
        while left_idx <= right_idx:
            middle_idx = (left_idx + right_idx) // 2
            middle_number = nums[middle_idx]
            if target == middle_number:
                return middle_idx
            if target > middle_number :
                left_idx = middle_idx + 1 
            else:
                right_idx = middle_idx - 1
        return 1