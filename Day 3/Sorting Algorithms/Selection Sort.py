l = list(map(int,input().strip().split(',')))
n = len(l)

for i in range(n-1):
    min_i = i
    for j in range(i+1,n):
        if l[min_i]>l[j]:
            min_i = j
    
    temp = l[i]
    l[i] = l[min_i]
    l[min_i] = temp
    print(l)

print(l)