def search(l,key):
    for i in range(len(l)):
        if l[i][0]>key:
            for j in range(len(l[i-1])):
                if l[i-1][j]==key:
                    return (i-1,j)
    for i in range(len(l[len(l)-1])):
        if key==l[len(l)-1][i]:
            return (len(l)-1,i)
    return -1


l = [[1,2,3,4],[11,12,13,14],[21,22,23,24],[31,32,33,34]]
key = 34
print(search(l,key))