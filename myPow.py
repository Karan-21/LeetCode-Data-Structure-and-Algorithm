class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:

            x = 1 / x

            n = abs(n)

        return self.solve(x,n)
    
    def solve(self,x,n):

        if n == 0:
            return 1
        
        half = self.solve(x,n//2)

        if n % 2 == 0:
            return half * half
        
        else:
            return x * (half * half)
