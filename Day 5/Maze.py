def maze(l1,l2):
    if l1[0]>l2[0] or l1[1]>l2[1]:
        return 0
    if l1[0]==l2[0] and l1[1]==l2[1]:
        return 1
    return maze([l1[0]+1,l1[1]],[l2[0],l2[1]])+ maze([l1[0],l1[1]+1],[l2[0],l2[1]])
    

print(maze([0,0],[2,2]))