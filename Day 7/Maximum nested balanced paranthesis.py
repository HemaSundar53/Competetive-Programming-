def balanced(s):
    l = []
    c,m = 0,0
    for i in s:
        if i=='(':
            l.append(i)
            c+=1
        elif i==')':
            if l[-1]=='(':
                c-=1
                l.pop()
            else:
                return -1
        else:
            continue
        m = max(c,m)
    return m
    
st = input()
print(balanced(st))