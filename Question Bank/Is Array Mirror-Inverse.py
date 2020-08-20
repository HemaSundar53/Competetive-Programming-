def mirror_inverse(l):
    for i in range(len(l)):
        if l[i]!=l.index(i):
            return False
    return True
    

l = list(map(int,input().strip().split(',')))
print(mirror_inverse(l))