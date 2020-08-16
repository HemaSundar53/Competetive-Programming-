def first_neg(nums,k):
    l = []
    for i in range(len(nums)-k+1):
        t = 0
        for j in nums[i:i+k]:
            if j<0:
                t = j
                break
        l.append(t)

    return l


lis = list(map(int,input().strip().split()))
k = int(input())
print(first_neg(lis,k))