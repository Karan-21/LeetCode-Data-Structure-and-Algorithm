class Solution:
    def maxProduct(self, root):
        def dfs(node):
            if not node: return 0
            ans = dfs(node.left) + dfs(node.right) + node.val
            res.append(ans)
            return ans
        
        res = []
        dfs(root)
        sum_all = max(res)
        return max(i*(sum_all-i) for i in res) % (10**9 + 7)
