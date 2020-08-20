def detectCycle(self, head):
    if head==None or head.next==None:
        return None
    
    slow = head
    fast = head
    val = 0
        
    while fast and slow:
        slow = slow.next
        if not fast.next:
            return
        fast = fast.next.next
        if slow==fast:
            val = 1
            break
        
    if not val:
        return
    slow = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
        
    return slow