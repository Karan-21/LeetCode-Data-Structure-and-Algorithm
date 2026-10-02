class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(stack, open, close):

            if open == close == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                dfs(stack, open + 1, close)
                stack.pop()
            
            if close < open:
                stack.append(")")
                dfs(stack, open, close + 1)
                stack.pop()
            
        dfs([],0,0)

        return res
