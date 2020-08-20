def getIntersectionNode(headA, headB):
    A = headA
    B = headB
    
    while A!=B:
        if A:
            A = A.next
        else:
            A = headB
        if B:
            B = B.next
        else:
            B = headA
  
    return A