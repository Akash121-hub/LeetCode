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