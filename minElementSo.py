class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            s = str(nums[i])
            for j in s:
                ans[i] += int(j)
        return min(ans)
