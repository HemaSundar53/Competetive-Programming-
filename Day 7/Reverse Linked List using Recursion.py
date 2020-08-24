def reverseList(head):
    if head==None or head.next==None:
        return head
    ll = reverseList(head.next)
    head.next.next = head
    head.next = None
    return ll