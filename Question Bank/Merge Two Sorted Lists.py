def mergeTwoLists(self, l1, l2):
    M = N = ListNode()
    while l1 and l2:
        if l1.val<=l2.val:
            N.next = ListNode(l1.val)
            N = N.next
            l1 = l1.next
        else:
            N.next = ListNode(l2.val)
            N = N.next
            l2 = l2.next

    while l1:
        N.next = ListNode(l1.val)
        N = N.next
        l1 = l1.next
    while l2:
        N.next = ListNode(l2.val)
        N = N.next
        l2 = l2.next
        
    return M.next