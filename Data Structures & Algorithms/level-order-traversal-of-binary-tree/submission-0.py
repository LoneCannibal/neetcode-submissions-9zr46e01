# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        res =[]
        if not root:
            return res
        queue.append(root)

        while(queue):
            qlen = len(queue)
            for i in range(qlen):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)

            level=[]
            for i in range(qlen):
                level.append(queue.pop(0).val)
            res.append(level)

        return res

        