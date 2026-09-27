class Solution:
    def reverseParentheses(self, s: str) -> str:
        s1 = s
        for i in range(s.count("(")):
            end = s1.find(")")
            start = s1.rfind("(",0,end)
            mid = s1[start+1:end]
            s1 = s1.replace(f"({mid})",mid[::-1])
        return s1  
            
