class Solution:
    def checkValidString(self, s: str) -> bool:

        openCount = closeCount = 0

        n = len(s)

        for i in range(n):

            if s[i] == "(" or s[i] == "*":
                openCount += 1
            
            else:
                openCount -= 1
            
            if s[n-i-1] == ")" or s[n-i-1] == "*":
                closeCount += 1
            
            else:
                closeCount -= 1
            
            if openCount < 0 or closeCount < 0:
                return False
        
        return True
