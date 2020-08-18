def maze(l1,l2,st):
    if l1[0]>l2[0] or l1[1]>l2[1]:
        return
    if l1[0]==l2[0] and l1[1]==l2[1]:
        print(st)
        return
    maze([l1[0]+1,l1[1]],[l2[0],l2[1]],st+'V ')
    maze([l1[0],l1[1]+1],[l2[0],l2[1]],st+'H ')
    maze([l1[0]+1,l1[1]+1],[l2[0],l2[1]], st+'D ')
    

maze([0,0],[2,2],'')