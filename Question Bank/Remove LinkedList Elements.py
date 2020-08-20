def removeElements(head, val):
    while head and head.val==val:
        head = head.next
    N = head
    while N and N.next:
        if N.next.val==val:
            N.next = N.next.next
        else:
            N = N.next
    return head