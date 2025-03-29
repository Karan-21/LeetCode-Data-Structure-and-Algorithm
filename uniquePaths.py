class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        return self.recurr(m,n,0,0,{})
    
    def recurr(self,m,n,i,j,dp):

        if i>=m or j>=n:
            return 0
        
        if i == m-1 and j == n-1:
            return 1
        
        if (i,j) in dp:
            return dp[(i,j)]
        
        case1 = self.recurr(m,n,i+1,j,dp)

        case2 = self.recurr(m,n,i,j+1,dp)

        dp[(i,j)] = case1 + case2

        return dp[(i,j)]
