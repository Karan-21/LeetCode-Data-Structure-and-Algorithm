class Solution:
    def minimumDeletions(self, s: str) -> int:

        totalA = 0
        n = len(s)

        for i in range(n):
            if s[i] == 'a':
                totalA += 1
        
        res = float('inf')
        leftB = 0

        for i in range(n):

            if s[i] == 'a':
                totalA -= 1
            
            res = min(res, totalA + leftB)

            if s[i] == 'b':
                leftB += 1
        
        return res
