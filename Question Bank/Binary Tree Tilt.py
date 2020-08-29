class Solution(object):
    def __init__(self):
        self.s = 0

    def findTilt(self, root):
        self.tree(root)
        return self.s
    
    def tree(self, node):
        if not node:
            return 0
        l = self.tree(node.left)
        r = self.tree(node.right)
        self.s += abs(l-r)
        return node.val+l+r