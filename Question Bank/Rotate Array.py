nums = list(map(int,input().strip().split(',')))
k = int(input())

for i in range(k):
    nums.insert(0,nums.pop())

print(nums)