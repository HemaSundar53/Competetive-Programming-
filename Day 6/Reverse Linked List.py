def reverseList(head):
    cur = head
    temp = None
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    head = prev
    return head
