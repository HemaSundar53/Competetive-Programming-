def deleteDuplicates(head):
    d = {}
    cur = head
    while cur:
        if cur.val in d:
            d[cur.val]+=1
        else:
            d[cur.val]=1
        cur = cur.next
    l = []
    for k,v in d.items():
        if v==1:
            l.append(k)
    A = B = ListNode()
    for i in sorted(l):
        A.next = ListNode(i)
        A = A.next
    return B.next