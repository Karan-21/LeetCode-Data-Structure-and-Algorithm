class Solution:
    def minOperations(self, s: str) -> int:
        return min(q:=sum(a!=b for a,b in zip(s,cycle('01'))), len(s)-q)
