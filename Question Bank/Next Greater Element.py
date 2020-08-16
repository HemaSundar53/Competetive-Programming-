def nextGreaterElement(nums1, nums2):
    l = []
    for i in range(len(nums1)):
        t = -1
        for j in range(nums2.index(nums1[i])+1,len(nums2)):
            if nums1[i]<nums2[j]:
                t = nums2[j]
                break
        l.append(t)
    return l
        
l1 = list(map(int, input().strip().split()))
l2 = list(map(int, input().strip().split()))
print(nextGreaterElement(l1,l2))