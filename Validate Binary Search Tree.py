# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.valid(root, float('-inf'), float('inf'))
    
    def valid(self,root,mini,maxi):

        if not root:
            return True
        
        if root.val <= mini or root.val >= maxi:
            return False
        
        leftV = self.valid(root.left, mini, root.val)
        rightV = self.valid(root.right, root.val, maxi)

        return leftV and rightV
