l = list(map(int, input().strip().split()))
temp = -1

for i in range(len(l)):
    if sum(l[:i])==sum(l[i+1:]):
        temp = i
        break
print(temp)