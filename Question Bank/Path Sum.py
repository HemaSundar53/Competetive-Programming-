def hasPathSum(root, sum):
    if not root:
        return 0
    if not root.left and not root.right:
        return sum==root.val
    return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)