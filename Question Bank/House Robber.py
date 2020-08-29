def rob(nums):
    a,b = 0,0
    for i in nums:
        a,b = b,max(a+i,b)
            
    return b