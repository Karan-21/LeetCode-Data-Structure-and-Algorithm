class Solution:
    def maxDistance(self, c: List[int]) -> int:
        return next(max(i, len(c)-i-1) 
            for i in range((len(c)+1)//2)
            if  c[i] != c[-1]  or  c[0] != c[-1-i]
        )
        
