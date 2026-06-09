class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_val = 0
        min_val = float('inf')

        for num in nums:
            max_val = max(max_val, num)
            min_val = min(min_val, num)

        return k * (max_val - min_val)
