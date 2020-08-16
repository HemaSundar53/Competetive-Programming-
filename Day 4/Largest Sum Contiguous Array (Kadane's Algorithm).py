def maxSubArray(nums):
    for i in range(len(nums)):
        if nums[i]>=0:
            break
        if i==len(nums)-1:
            return max(nums)
    
    # Kadane's Algo    
    cs=0
    ms=0
    for i in nums:
        cs+=i
        if cs<0:
            cs=0
        ms=max(cs,ms)
    return ms
    
l = list(map(int,input().strip().split(',')))
print(maxSubArray(l))