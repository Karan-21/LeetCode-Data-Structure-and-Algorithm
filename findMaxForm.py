class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        return self.recurr(strs,m,n,0,{})
    
    def recurr(self,strs,m,n,idx,dp):

        if idx >= len(strs):
            return 0
        
        if (m,n,idx) in dp:
            return dp[(m,n,idx)]
        
        mCount = strs[idx].count("0")
    
        nCount = strs[idx].count("1")

        # SKIP
        dp[(m,n,idx)] = self.recurr(strs,m,n,idx+1,dp)

        # IN-BOUND
        if mCount <= m and nCount <= n:

            # INCLUDE => Max(Current, 1 + After Including it)
            dp[(m,n,idx)] = max(self.recurr(strs,m,n,idx,dp), 
                1 + self.recurr(strs,m - mCount,n - nCount,idx+1,dp))

        return dp[(m,n,idx)]
