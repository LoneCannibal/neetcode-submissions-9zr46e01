# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(r, sR):
            if not r and not sR:
                return True
            if not r or not sR:
                return False
            if r.val!=sR.val:
                return False
            #print("sameTree",r.val,sR.val)
            return sameTree(r.left, sR.left) and sameTree(r.right, sR.right)
        
        if not root and not subRoot:
            return True
        if not root:
            return False
        #print(root.val, subRoot.val, sameTree(root,subRoot), root.val ==subRoot.val)
        if root.val ==subRoot.val and sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        