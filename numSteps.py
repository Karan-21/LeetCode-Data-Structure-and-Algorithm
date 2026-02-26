class Solution:
    def numSteps(self, s: str) -> int:

        n = len(s)

        steps = 0

        carry = 0

        for i in range(n-1,0,-1):

            digit = int(s[i]) + carry

            if digit % 2 == 1:
                # For Odd Number => Last bit is 1
                # First, Add 1 to make it Even => +1
                # Secondly, Divide it by 2 or Right Shift to reduce ONE => +1
                steps += 2
                carry = 1
            
            else:
                # If it's already Even => Just Do Right Shift or Divide by 2 => +1
                steps += 1
        
        return steps + carry
