class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        n = len(values)

        dp = [[-1 for i in range(n)] for j in range(n)]

        return self.solveMemo(values, 0, n-1, dp)
    
    def solveMemo(self,val,i,j, dp):

        if i+1 == j:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        ans = float('inf')

        for k in range(i+1,j):

            ans = min(ans, val[i] * val[j] * val[k] + self.solveMemo(val,i,k, dp) + self.solveMemo(val,k,j, dp))
        
        dp[i][j] = ans
        
        return dp[i][j]
