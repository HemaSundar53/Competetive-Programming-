def isSymmetric(root):
    return mirror(root,root)
    
def mirror(A,B):
    if not A and not B:
        return True
    if not A or not B:
        return False
    return (A.val==B.val) and mirror(A.left,B.right) and mirror(A.right,B.left)