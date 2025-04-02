# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        return self.solve(root, targetSum, 0)
    
    def solve(self,root,targetSum,summ):

        if not root:
            return False
        
        summ += root.val

        if not root.left and not root.right:

            if summ == targetSum:
                return True
            
            else:
                return False
        
        return self.solve(root.left, targetSum, summ) or self.solve(root.right, targetSum, summ)
