class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        prev = float("-inf")
        for i in nums:
            if prev < i - k:
                prev = i - k
                res += 1
            elif prev < i + k:
                prev = prev + 1
                res += 1
        return res
