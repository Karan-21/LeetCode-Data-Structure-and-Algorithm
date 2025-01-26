class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        buy = nums[0]

        maxi = 0

        for i in range(1,len(nums)):

            pro = nums[i] - buy

            maxi = max(maxi, pro)

            buy = min(buy, nums[i])
        
        return maxi
