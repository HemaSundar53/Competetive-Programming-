l = list(map(int,input().strip().split(',')))
n = len(l)

for i in range(1,n):
    v = l[i]
    j = i
    
    while j>0 and l[j-1]>v:
        l[j] = l[j-1]
        j -= 1
    l[j] = v
  
print(l)