# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestorp, ancestorq=[], []
        def traverse(node, v, ancestor):
            ancestor.append(node)
            if node.val == v.val:
                return
            if node.val > v.val:
                traverse(node.left,v, ancestor)
            else:
                traverse(node.right,v, ancestor)
        traverse(root,p,ancestorp)
        traverse(root, q,ancestorq)
        
        res = None
        for i in range(min(len(ancestorp), len(ancestorq))):
            if ancestorp[i] != ancestorq[i]:
                break
            res = ancestorp[i]
        return res