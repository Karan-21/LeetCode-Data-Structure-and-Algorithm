class Solution:
    def reverse(self, x: int) -> int:

        sign = True

        if x < 0:
            sign = False
        
        x = abs(x)

        ans = 0

        while x != 0:
            digit = x % 10
            
            # Special Case
            if ans > (2**31 - 1) // 10 or ans < -2**31 // 10:
                return 0
            
            ans = (ans * 10) + digit
            x = x // 10
        
        if sign == False:
            return -1 * ans

        return ans
