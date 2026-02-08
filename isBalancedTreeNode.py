# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True

        def dfs(root):

            if not root:
                return self.res
            
            lh = dfs(root.left)
            rh = dfs(root.right)

            if abs(lh-rh) > 1:
                self.res = False
            
            return 1 + max(lh, rh)
        
        dfs(root)

        return self.res
