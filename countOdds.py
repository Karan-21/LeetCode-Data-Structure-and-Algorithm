class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=high-low+1
        if(low%2!=0 and high%2!=0):
            b=a//2+1
        else:
            b=a//2
        
        return(b)
