class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subArray = nums[i:j+1]
                ans += (len(set(subArray)))**2
        return ans
