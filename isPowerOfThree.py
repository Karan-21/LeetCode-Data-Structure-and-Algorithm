class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0:
            return False

        if n % 3 == 0:
            return True
        
        else:
            return False
