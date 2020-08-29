def searchBST(root, val):
    if not root:
        return
    if root.val==val:
        return root
    return searchBST(root.left,val) or searchBST(root.right,val)