# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue=[]
        res =[]

        if not root:
            return []
        queue.append(root)

        while(queue):
            qlen = len(queue)
            level=[]
            for i in range(qlen):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                level.append(current.val)
                if i== qlen-1:
                    res.append(current.val)
        
        
        return res
                

        