class Solution:
    def makeFancyString(self, s: str) -> str:
        return re.sub(r'(.)\1+',r'\1\1',s)
