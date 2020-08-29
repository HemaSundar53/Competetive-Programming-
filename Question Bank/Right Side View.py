def rightSideView(root):
    if root==None:
        return []
    ans=[root.val]
    left=ans+self.rightSideView(root.left)
    right=ans+self.rightSideView(root.right)
    if len(right)>=len(left):
        return right
    return right+left[len(right):]