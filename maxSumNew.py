class Solution:
    def maxSum(self, a: List[int]) -> int:
        return sum(v for v in {*a} if v>0) or max(a)
