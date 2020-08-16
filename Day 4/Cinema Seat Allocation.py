def maxNumberOfFamilies(n, reservedSeats):
    c = 2*n
    d = {}
    for i in reservedSeats:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            l = [i[1]]
            d[i[0]] = l

    for i in d:
        
        l = False
        m = False
        r = False

        if 2 in d[i] or 3 in d[i] or 4 in d[i] or 5 in d[i]:
            l = True
        if 4 in d[i] or 5 in d[i] or 6 in d[i] or 7 in d[i]:
            m = True
        if 6 in d[i] or 7 in d[i] or 8 in d[i] or 9 in d[i]:
            r = True
            
        if l:
            c -= 1
        if r:
            c -= 1
        if l and r and (not m):
            c += 1
        
    return c
    

n = int(input())
s = input().split(',')
l = []
for i in range(0,len(s)-1,2):
    l.append([int(s[i]),int(s[i+1])])
print(maxNumberOfFamilies(n, l))
