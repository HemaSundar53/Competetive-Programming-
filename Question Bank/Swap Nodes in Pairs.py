def swapPairs(head):
    cur = head
    while cur and cur.next:
        cur.val,cur.next.val = cur.next.val,cur.val
        cur = cur.next.next
    return head