def shuffle(nums, n):
    l=[]
    for i in range(n):
        l.append(nums[i])
        l.append(nums[i+n])
    return l

arr = list(map(int, input().strip().split()))
n = int(input())
print(shuffle(arr,n))