def merge(l):
    
    if len(l)>1:
        L = l[:len(l)//2]
        R = l[len(l)//2:]
        
        L = merge(L)
        R = merge(R)
        
        l = []
        while len(L)>0 and len(R)>0:
            if L[0]<R[0]:
                l.append(L.pop(0))
            else:
                l.append(R.pop(0))
    
        for i in L:
            l.append(i)
        for i in R:
            l.append(i)
    
    return l


lis = list(map(int,input().strip().split(',')))
print(merge(lis))
