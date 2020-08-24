def mergeKLists(lists):
    l = []
    for i in lists:
        while i:
            l.append(i.val)
            i = i.next
        
    A = B = ListNode()
    for i in sorted(l):
        B.next = ListNode(i)
        B = B.next
    return A.next