class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        lastTwo = defaultdict(lambda: [-inf, -inf])
        minD = inf
        for i, n in enumerate(nums):
            minD = min(minD, (i - lastTwo[n][1]) * 2)
            lastTwo[n][1] = lastTwo[n][0]
            lastTwo[n][0] = i
        return -1 if minD == inf else minD
