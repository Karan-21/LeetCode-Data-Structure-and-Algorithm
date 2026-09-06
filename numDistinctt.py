class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        return self.recurr(s,t,0,0,{})
    
    def recurr(self,a,b,i,j,dp):

        if j >= len(b):
            return 1
        
        if i >= len(a):
            return 0
        
        if (i,j) in dp:
            return dp[(i,j)]
        
        if a[i] == b[j]:
            dp[(i,j)] = self.recurr(a,b,i+1,j+1,dp) + self.recurr(a,b,i+1,j,dp)
        
        else:
            dp[(i,j)] = self.recurr(a,b,i+1,j,dp)
        
        return dp[(i,j)]
