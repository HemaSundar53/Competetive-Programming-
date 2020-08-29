def maxDepth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))