class Solution:
    def climbStairs(self, n: int) -> int:
        return self.recurr(n,{})
    
    def recurr(self,n,dp):

        if n == 0:
            return 1
        
        if n < 0:
            return 0

        if n in dp:
            return dp[n]
        
        dp[n] = self.recurr(n-1, dp) + self.recurr(n-2, dp)

        return dp[n]
