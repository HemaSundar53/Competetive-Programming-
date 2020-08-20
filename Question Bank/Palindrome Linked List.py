def isPalindrome(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
        
    return l==l[::-1]