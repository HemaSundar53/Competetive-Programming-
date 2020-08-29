def deleteDuplicates(head):
    a = head
    while a and a.next:
        if a.val == a.next.val:
            a.next = a.next.next
        else:
            a = a.next
    return head