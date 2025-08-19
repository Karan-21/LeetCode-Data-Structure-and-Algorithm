class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        for n in nums:
            if n == 0:
                cnt += 1
            else:
                ans += cnt * (cnt + 1) // 2
                cnt = 0
        ans += cnt * (cnt + 1) // 2
        return ans
