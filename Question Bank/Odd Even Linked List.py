def oddEvenList(head):
    if head==None or head.next==None:
        return head
    odd = head
    evenhead = even = ListNode()
    while odd and odd.next:
        even.next = ListNode(odd.next.val)
        even = even.next
        odd.next = odd.next.next
        if odd.next:
            odd = odd.next

    odd.next = evenhead.next
        
    return head