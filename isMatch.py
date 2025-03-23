class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # return self.solveRecurr(s,p,len(s)-1,len(p)-1)

        dp = [[-1 for i in range(len(p)+1)] for j in range(len(s)+1)]

        return self.solveMemo(s,p,len(s)-1,len(p)-1,dp)
    
    def solveRecurr(self,s,p,i,j):

        if i<0 and j<0:
            return True
        
        if i>=0 and j<0:
            return False
        
        if i<0 and j>=0:
            for k in range(j+1):
                if p[k] != "*":
                    return False
            return True
    
        if s[i] == p[j] or p[j] == "?":
            return self.solveRecurr(s,p,i-1,j-1)
        
        elif p[j] == "*":

            return self.solveRecurr(s,p,i-1,j) or self.solveRecurr(s,p,i,j-1)

        else:
            return False
