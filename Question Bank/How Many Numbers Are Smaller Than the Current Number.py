def smallerNumbersThanCurrent(nums):
    c = [0]*(max(nums)+2)
    for i in nums:
        c[i+1]+=1
    for i in range(1,max(nums)+1):
        c[i]+=c[i-1]
            
    return [c[i] for i in nums]

arr = list(map(int, input().strip().split()))
print(smallerNumbersThanCurrent(arr))