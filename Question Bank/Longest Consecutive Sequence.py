def longestConsecutive(nums):
    if nums==[]:
        return 0
    d = {}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        
    l = []
    for i in d:
        l.append(i)
    l.sort()
    
    c,m = 1,1
    for i in range(len(l)-1):
        if l[i]+1==l[i+1]:
            c+=1
        else:
            m = max(c,m)
            c = 1
    
    m = max(c,m)
    return m
    

l = list(map(int,input().strip().split(',')))
print(longestConsecutive(l))