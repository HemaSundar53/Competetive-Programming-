def addTwoNumbers(l1, l2):
    s1,s2 = '',''
    while l1:
        s1 += str(l1.val)
        l1 = l1.next
    while l2:
        s2 += str(l2.val)
        l2 = l2.next

    n = int(s1[::-1])+int(s2[::-1])
    l = L = ListNode()
    if n==0:
        return l
        
    while n!=0:
        L.next = ListNode(n%10)
        n /= 10
        L = L.next
            
    return l.next