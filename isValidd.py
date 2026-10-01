class Solution:
    def isValid(self, s: str) -> bool:

        dict = {")":"(", "}":"{", "]":"["}

        stack = []

        for i in range(len(s)):

            if s[i] in dict.values():
                stack.append(s[i])
            
            elif stack and stack[-1] == dict[s[i]]:
                stack.pop()
            
            else:
                return False
        
        return stack == []
