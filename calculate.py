class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        res = 0
        stack = []
        sign = 1

        for char in s:

            if char.isdigit():
                curr = curr * 10 + int(char)
            
            elif char in ['+','-']:
                res += sign * curr

                sign = 1 if char == '+' else -1
            
                curr = 0
            
            elif char == "(": 
                stack.append(res)
                stack.append(sign)

                sign = 1

                res = 0
            
            elif char == ")":
                res += sign * curr

                res *= stack.pop()

                res += stack.pop()

                curr = 0
            
        return res + sign * curr
