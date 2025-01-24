class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictS = {}

        for i in range(len(s)):

            if s[i] not in dictS:
                dictS[s[i]] = 1
            
            else:
                dictS[s[i]] += 1
        
        for i in range(len(t)):

            if t[i] not in dictS:
                return False
            
            else:

                if dictS[t[i]] == 0:
                    return False
                
                dictS[t[i]] -= 1
        
        for i in dictS:
            if dictS[i] != 0:
                return False
        
        return True
