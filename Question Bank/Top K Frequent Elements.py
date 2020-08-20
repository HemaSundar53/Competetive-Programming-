def topKFrequent(nums, k):
    d = {}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    l = []
    sort_d= sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(sort_d)):
        if k==i:
            break
        l.append(sort_d[i][0])
    return l
    

l = list(map(int,input().strip().split(',')))
n = int(input())
print(topKFrequent(l,n))