# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = float('-inf')

        def dfs(root):

            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)

            ans = lh + rh + root.val

            ifNeg = max(lh, rh) + root.val

            only = root.val

            self.res = max(self.res, ans, ifNeg, only)

            return max(ifNeg, only)
        
        dfs(root)

        return self.res
