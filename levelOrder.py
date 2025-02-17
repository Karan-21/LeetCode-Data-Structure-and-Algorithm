# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None
        
        queue = [root]

        res = []

        while queue:

            layers = []

            for i in range(len(queue)):

                temp = queue.pop(0)

                layers.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
            
            res.append(layers)
        
        return res
