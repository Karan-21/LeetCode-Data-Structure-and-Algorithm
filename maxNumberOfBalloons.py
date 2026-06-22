class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        l=[]
        l.append(text.count("b"))
        l.append(text.count("a"))
        l.append(text.count("l")//2)
        l.append(text.count("o")//2)
        l.append(text.count("n"))
        return min(l)
