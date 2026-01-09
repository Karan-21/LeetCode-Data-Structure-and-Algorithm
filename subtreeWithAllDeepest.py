class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
                               
        def dfs(node = root, level = 0):
            if not node:
                return level-1
            
            l, r = dfs(node.left, level+1), dfs(node.right, level+1)
            
            if l == r:
                d[l] = node
                
            return max(l,r)
        
        d = {}
        return d[dfs()]
