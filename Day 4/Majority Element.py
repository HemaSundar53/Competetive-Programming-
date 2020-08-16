def majorityElement(nums):
    d={}
    for i in nums:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for k,v in d.items():
        if v>len(nums)/2:
            return k
            
l = list(map(int,input().strip().split(',')))
print(majorityElement(l))