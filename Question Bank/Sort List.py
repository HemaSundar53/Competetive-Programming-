def sortList(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
        
    l.sort()
    L = ll = ListNode()
    while l:
        ll.next = ListNode(l.pop(0))
        ll = ll.next
    return L.next