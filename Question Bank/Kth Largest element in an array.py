def findKthLargest(nums, k):
    key = 1
    for i in reversed(sorted(nums)):
        if key == k:
            return i
        key+=1

l = list(map(int, input().strip().split()))
n = int(input())
print(findKthLargest(l,n))