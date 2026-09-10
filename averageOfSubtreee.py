# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        self.ans = 0

        def dfs(root):

            if not root:
                return [0,0] # Sum, Count
            
            leftP = dfs(root.left)
            rightP = dfs(root.right)

            summ = root.val + leftP[0] + rightP[0]

            count = 1 + leftP[1] + rightP[1]

            avg = summ // count

            if avg == root.val:
                self.ans += 1
            
            return [summ, count]
        
        dfs(root)

        return self.ans
