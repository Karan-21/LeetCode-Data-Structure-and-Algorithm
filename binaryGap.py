class Solution:
    def binaryGap(self, n: int) -> int:
        maxi = 0
        last = float('inf')
        i = 0
        while n:
            if n & 1:
                if i-last > maxi :
                    maxi = i-last
                last = i
            n >>= 1
            i+=1
        return maxi
