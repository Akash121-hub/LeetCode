nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6,0,0,0]

num3 = []

for i in range(len(nums1)):
    if nums1[i] > nums2[i]:
        num3.append (nums2[i])
        num3.append(nums1[i])
    else:
        num3.append(nums1[i])

print(num3)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
            
                