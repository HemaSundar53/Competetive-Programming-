def zigzag(l):
    c = 0
    for i in range(len(l)-1):
        if i%2==0:
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
                c+=1
        else:
            if l[i]<l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
                c+=1
    return (l,c)

    
arr = list(map(int,input().strip().split(',')))
print(zigzag(arr))