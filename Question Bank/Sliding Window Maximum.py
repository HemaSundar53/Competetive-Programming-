def maxSlidingWindow(nums, k):
    l = []
    for i in range(len(nums)-k+1):
        
        l.append(max(nums[i:i+k]))
    return l