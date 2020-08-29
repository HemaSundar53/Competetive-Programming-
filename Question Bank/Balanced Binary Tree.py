def isBalanced(root):
    if not root:
        return 1
    return (abs(length(root.left)-length(root.right))<=1)and self.isBalanced(root.left) and self.isBalanced(root.right)
        
def length(node):
    if not node:
        return 0
    return 1+max(length(node.right),length(node.left))