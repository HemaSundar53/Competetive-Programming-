def removeDuplicates(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i]!=nums[k]:
            k+=1
            nums[k]=nums[i]
    return k+1
    
l = list(map(int,input().strip().split(',')))
print(l[:removeDuplicates(l)])